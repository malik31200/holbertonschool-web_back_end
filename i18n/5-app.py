#!/usr/bin/env python3
"""
Basic Flask app with Babel selection.
"""

from flask import Flask, render_template, request, g
from flask_babel import Babel


class Config:
    """
    Configuration class for Babel.
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)

babel = Babel()


users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


def get_locale():
    """Determine the best language match"""
    locale = request.args.get("locale")

    if locale and locale in app.config["LANGUAGES"]:
        return locale
    return request.accept_languages.best_match(app.config["LANGUAGES"])


babel.init_app(app, locale_selector=get_locale)


def get_user():
    """Return user dictionary or None"""
    user_id = request.args.get("login_as")

    if user_id:
        return users.get(int(user_id))

    return None


@app.before_request
def before_request():
    """Set logged user"""
    g.user = get_user()


@app.route('/')
def index() -> str:
    """
    Display the home page
    """
    return render_template("5-index.html")


if __name__ == "__main__":
    app.run(debug=True)
