#!/usr/bin/env python3
"""
SessionAuth module
"""

from .auth import Auth
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
