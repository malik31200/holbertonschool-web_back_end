#!/usr/bin/env python3
"""
Module that filters sensitive fields in log messages
"""
import os
import logging
import re
import mysql.connector


from typing import List
from mysql.connector import connection


PII_FIELDS = ("name", "email", "phone", "ssn", "password")


class RedactingFormatter(logging.Formatter):
    """
    Formatter that filters sensitive data from log messages.
    """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        """
        Initialize formatter with fields to redact
        """
        super().__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        """
         Format log record and redact sensitive fields.
        """
        original = super().format(record)
        return filter_datum(self.fields, self.REDACTION,
                            original, self.SEPARATOR)


def filter_datum(fields: List[str],
                 redaction: str,
                 message: str,
                 separator: str) -> str:
    """
    Obfuscates sensitive fields in a log message.

    Args:
        fields: list of fields to obscufates(password, date of birth).
        redaction: used to remplace sensitive data.
        message: original log message.
        separator: character separating fields in the message.

    Returns:
        str: message with sensitive fields obfuscated
    """
    for field in fields:
        pattern = f"{field}=.*?{separator}"
        remplacement = f"{field}={redaction}{separator}"
        message = re.sub(pattern, remplacement, message)
    return message


def get_logger() -> logging.Logger:
    """
    Create and return a configured logger.
    """
    # Create a logger named "user_data"
    logger = logging.getLogger("user_data")

    # The logger only display INFO and more important messages
    logger.setLevel(logging.INFO)

    # Prevent messages from being sent to parent loggers
    logger.propagate = False

    # Hander display the logs in terminal
    handler = logging.StreamHandler()

    # Combines our formatter which hides sensitive data
    handler.setFormatter(
        RedactingFormatter(PII_FIELDS)
    )

    # Attach the handler to the Logger
    logger.addHandler(handler)

    return logger


def get_db() -> connection.MySQLConnection:
    """
    Return a connexion to the MySQLConnection
    """
    return mysql.connector.connect(
        user=os.getenv("PERSONAL_DATA_DB_USERNAME", "root"),
        password=os.getenv("PERSONAL_DATA_DB_PASSWORD", ""),
        host=os.getenv("PERSONAL_DATA_DB_HOST", "localhost"),
        database=os.getenv("PERSONAL_DATA_DB_NAME")
    )


def main() -> None:
    """
    Retrieve user records from the database and log them
    """
    # Create the logger
    logger = get_logger()

    # Connexion to the database
    db = get_db()

    # Create a curor to axecute SQL query
    cursor = db.cursor()

    # Retrieve  all rows from the users tble
    cursor.execute("SELECT * FROM users;")

    # Get the column names from the query results
    columns = [col[0] for col in cursor.description]

    # Iterate through each row returned by the query
    for row in cursor:
        message = "; ".join(
            f"{column}={value}"
            for column, value in zip(columns, row)
        ) + ";"

        logger.info(message)

    cursor.close()
    db.close()


if __name__ == "__main__":
    main()
