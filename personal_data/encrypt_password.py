#!/usr/bin/env python3
"""
 function that expects one string argument name password and returns a salted
"""


import bcrypt


def hash_password(password: str) -> bytes:
    """
    Hash a password using bcrypt and a random salt
    """
    return bcrypt.hashpw(
        password.encode("utf-8"),
        bcrypt.gensalt()
    )


def is_valid(hashed_password: bytes, password: str) -> bool:
    """Validate that a password matches its hashed version."""
    return bcrypt.checkpw(
        password.encode("utf-8"),
        hashed_password
    )
