#!/usr/bin/env python3
"""
Module that filters sensitive fields in log messages
"""
import re
import logging
from typing import List


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
        return filter_datum(self.fields, self.REDACTION, original, self.SEPARATOR)

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
