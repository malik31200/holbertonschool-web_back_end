#!/usr/bin/env python3
"""
Route module for the API
"""
from os import getenv
from api.v1.views import app_views
from flask import Flask, jsonify, abort, request
from flask_cors import (CORS, cross_origin)
import os


app = Flask(__name__)
app.register_blueprint(app_views)
CORS(app, resources={r"/api/v1/*": {"origins": "*"}})

# Auth initialization
auth = None

if getenv("AUTH_TYPE") == "auth":
    from api.v1.auth.auth import Auth


@app.errorhandler(404)
def not_found(error) -> str:
    """ Not found handler
    """
    return jsonify({"error": "Not found"}), 404


@app.errorhandler(401)
def unauthorized(error) -> str:
    """ Handle 401 error
    """
    return jsonify({"error": "Unauthorized"}), 401


@app.errorhandler(403)
def forbidden(error) -> str:
    """ Handle 403 error
    """
    return jsonify({"error": "Forbidden"}), 403


# Before request filter
@app.before_request
def before_request():
    """ Filter all incoming requests before routing """
    if auth is None:
        return None

    excluded_paths = [
        "/api/v1/status/",
        "/api/v1/unauthorized/",
        "/api/v1/forbidden/"
    ]

    # If route is public -> allow request
    if not auth.require_auth(request.path, excluded_paths):
        return

    # If no Authorization header -> 401
    if auth.authorization_header(request) is None:
        abort(401)

    # If user is not valid -> 403
    if auth.current_user(request) is None:
        abort(403)


if __name__ == "__main__":
    host = getenv("API_HOST", "0.0.0.0")
    port = getenv("API_PORT", "5000")
    app.run(host=host, port=port)
