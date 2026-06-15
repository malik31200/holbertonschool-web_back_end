#!/usr/bin/env python3
"""
Auth module
"""

from flask import request
from typing import List, TypeVar
import os


class Auth():
    """ Authentication class """
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """ Determine if authentication is required """
        if path is None:
            return True

        if not excluded_paths:
            return True

        if not path.endswith('/'):
            path += '/'

        for excluded_path in excluded_paths:
            if path == excluded_path:
                return False

        return True

    def authorization_header(self,
                             request=None) -> str:
        """ Returns Authorization header from request """
        if request is None:
            return None

        if "Authorization" not in request.headers:
            return None

        return request.headers.get("Authorization")

    def current_user(self, request=None) -> TypeVar('User'):
        """  Returns False for now """
        return None

    def session_cookie(self, request=None):
        """
        Returns a cookie value from a request
        """
        if request is None:
            return None

        # Retrieve the name of cookie from env variable
        cookie_name = os.getenv("SESSION_NAME")

        # Retrieve the value of cookie in the request
        return request.cookies.get(cookie_name)
