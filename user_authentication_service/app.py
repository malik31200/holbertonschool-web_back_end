#!/usr/bin/env python3
"""A basic flask app
"""

from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/", methods=["GET"])
def home():
    """
    Home route returning JSON message
    """
    return jsonify({"message": "Bievenue"})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
