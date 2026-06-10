#!/usr/bin/env python3
"""
BasicAuth module
"""
from api.v1.auth.auth import Auth
from typing import TypeVar, Tuple
import base64


class BasicAuth(Auth):
    """Basic Authentication class"""
    pass

    def extract_base64_authorization_header(self,
                                            authorization_header: str) -> str:
        """ return part of base64 of the authorization of header """
        if authorization_header is None:
            return None

        if not isinstance(authorization_header, str):
            return None

        prefix = "Basic "
        if not authorization_header.startswith(prefix):
            return None

        base64_part = authorization_header[len(prefix):]

        if base64_part == "":
            return None

        return base64_part

    def decode_base64_authorization_header(
            self, base64_authorization_header: str) -> str:
        """ returns the decoded value of a Base64 """
        if base64_authorization_header is None:
            return None

        if not isinstance(base64_authorization_header, str):
            return None

        try:
            # Convert string to bytes
            base64_bytes = base64_authorization_header.encode("utf-8")

            # Decode Base64 bytes
            decoded_bytes = base64.b64decode(base64_bytes)

            # Convert bytes to UTF-8 string
            decoded_string = decoded_bytes.decode("utf-8")

            return decoded_string

        except Exception:
            return None

    def extract_user_credentials(
            self, decoded_base64_authorization_header: str) -> Tuple[str, str]:
        """ returns the user email and password
        from the Base64 decoded value """
        if decoded_base64_authorization_header is None:
            return (None, None)

        if not isinstance(decoded_base64_authorization_header, str):
            return (None, None)

        if ":" not in decoded_base64_authorization_header:
            return (None, None)

        email, password = decoded_base64_authorization_header.split(":", 1)

        return (email, password)
