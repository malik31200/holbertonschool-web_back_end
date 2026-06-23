#!/usr/bin/env python3
"""Auth module
"""

from db import DB
from user import User
from sqlalchemy.orm.exc import NoResultFound
import bcrypt
import uuid


def _hash_password(password: str) -> bytes:
    """
    Hash a password using bcrypt
    """
    return bcrypt.hashpw(
        password.encode('utf-8'),
        bcrypt.gensalt()
    )


def _generate_uuid() -> str:
    """
    Generate a uuid string
    """
    return str(uuid.uuid4())


class Auth:
    """Auth class to interact with the authentication database.
    """

    def __init__(self):
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        """
        Registers a new user
        """
        try:
            self._db.find_user_by(email=email)

            raise ValueError(
                f"User {email} already exists"
            )

        except NoResultFound:
            hashed_password = _hash_password(password)

            return self._db.add_user(
                email,
                hashed_password.decode("utf-8")
            )

    def valid_login(self, email: str, password: str) -> bool:
        """
        Check if login is valid
        """
        try:
            user = self._db.find_user_by(email=email)

            return bcrypt.checkpw(
                password.encode("utf-8"),
                user.hashed_password.encode("utf-8")
            )

        except NoResultFound:
            return False

    def create_session(self, email: str) -> str:
        """
        Returns a session id
        """
        try:
            user = self._db.find_user_by(email=email)

            session_id = _generate_uuid()

            self._db.update_user(
                user.id,
                session_id=session_id
            )

            return session_id

        except NoResultFound:
            return None
