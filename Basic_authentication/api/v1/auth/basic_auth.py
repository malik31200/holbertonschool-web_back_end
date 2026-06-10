#!/usr/bin/env python3
"""
BasicAuth module
"""
from api.v1.auth.auth import Auth


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
        if not self.authorization_header.startswith(prefix):
            return None

        base64_part = authorization_header[len(prefix):]

        if base64_part == "":
            return None

        return base64_part
