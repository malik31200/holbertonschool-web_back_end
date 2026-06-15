#!/usr/bin/env python3
"""
SessionAuth module
"""

from .auth import Auth
from models.user import User
import uuid


class SessionAuth(Auth):
    """
    SessionAuth class
    that stores user session in memory
    """
    user_id_by_session_id = {}

    def create_session(self, user_id: str = None) -> str:
        """
        Create a Session ID dor a user_id
        """
        if user_id is None:
            return None

        if not isinstance(user_id, str):
            return None

        # Generate a ID session unique
        session_id = str(uuid.uuid4())

        # Store in dictionary
        self.user_id_by_session_id[session_id] = user_id

        return session_id

    def user_id_for_session_id(self, session_id: str = None) -> str:
        """
        Returns a User ID based on a session Id
        """
        if session_id is None:
            return None

        if not isinstance(session_id, str):
            return None

        return self.user_id_by_session_id.get(session_id)

    def current_user(self, request=None):
        """
        Returns a user instance based on a cookie value
        """
        if request is None:
            return None

        # retrieve id session from a cookie
        session_id = self.session_cookie(request)

        if session_id is None:
            return None

        # refind id user from session
        user_id = self.user_id_for_session_id(session_id)

        if user_id is None:
            return None

        # retrieve user in database
        user = User.get(user_id)

        return user
