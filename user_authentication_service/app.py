#!/usr/bin/env python3
"""A basic flask app
"""

from flask import Flask, jsonify, request, abort, make_response, redirect
from auth import Auth

app = Flask(__name__)

AUTH = Auth()


@app.route("/", methods=["GET"])
def home():
    """
    Home route returning JSON message
    """
    return jsonify({"message": "Bienvenue"})


@app.route("/users", methods=["POST"])
def users():
    """
    Register a user
    """
    email = request.form.get("email")
    password = request.form.get("password")

    try:
        AUTH.register_user(email, password)
        return jsonify({
            "email": email,
            "message": "user created"
        })

    except ValueError:
        return jsonify({
            "message": "email already registered"
        }), 400


@app.route("/sessions", methods=["POST"])
def login():
    """ Login user and create session"""
    email = request.form.get("email")
    password = request.form.get("password")

    if not AUTH.valid_login(email, password):
        abort(401)

    session_id = AUTH.create_session(email)

    response = make_response(jsonify({
        "email": email,
        "message": "logged in"
    }))

    response.set_cookie("session_id", session_id)

    return response


@app.route("/sessions", methods=["DELETE"])
def logout():
    """ Logout user and destroy session """
    session_id = request.cookies.get("session_id")

    user = AUTH.get_user_from_session_id(session_id)

    if user is None:
        abort(403)

    AUTH.destroy_session(user.id)

    return redirect("/")


@app.route("/profile", methods=["GET"])
def profile():
    """ Get user profil from a session id """
    session_id = request.cookies.get("session_id")

    user = AUTH.get_user_from_session_id(session_id)

    if user is None:
        abort(403)

    return jsonify({
        "email": user.email
    })


@app.route("/reset_password", methods=["POST"])
def get_reset_password_token():
    """ Generate reset password token"""
    email = request.form.get("email")

    try:
        token = AUTH.get_reset_password_token(email)

        return jsonify({
            "email": email,
            "reset_token": token
        }), 200

    except ValueError:
        abort(403)


@app.route("/reset_password", methods=["PUT"])
def update_password():
    """ Update the password """
    email = request.form.get("email")
    reset_token = request.form.get("reset_token")
    new_password = request.form.get("new_password")

    try:
        AUTH.update_password(reset_token, new_password)

        return jsonify({
            "email": email,
            "message": "Password updated"
        }), 200

    except ValueError:
        abort(403)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
