#!/usr/bin/env python3
"""
Module that filters sensitive fields in log messages
"""
import re


def filter_datum(fields, redaction, message, separator):
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
