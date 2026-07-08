#!/usr/bin/env python3
"""
Basic Flask app with Babel selection.
"""

from flask import Flask, render_template, request, g
from flask_babel import Babel
import pytz
from pytz.exceptions import UnknownTimeZoneError


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


def get_locale():
    """Select bestlocale"""
    locale = request.args.get("locale")

    if locale and locale in app.config["LANGUAGES"]:
        return locale

    if g.user:
        user_locale = g.user.get("locale")

        if user_locale in app.config["LANGUAGES"]:
            return user_locale

    locale = request.accept_languages.best_match(
        app.config["LANGUAGES"]
    )

    return locale or app.config["BABEL_DEFAULT_LOCALE"]


def get_timezone():
    """Get the best timezone"""

    timezone = request.args.get("timezone")

    if timezone:
        try:
            pytz.timezone(timezone)
            return timezone
        except UnknownTimeZoneError:
            pass

    if g.user:
        user_timezone = g.user.get("timezone")

        if user_timezone:
            try:
                pytz.timezone(user_timezone)
                return user_timezone
            except UnknownTimeZoneError:
                pass

    return app.config["BABEL_DEFAULT_TIMEZONE"]


babel.init_app(
    app, locale_selector=get_locale,
    timezone_selector=get_timezone
    )


@app.route('/')
def index() -> str:
    """
    Display the home page
    """
    return render_template("7-index.html")


if __name__ == "__main__":
    app.run(debug=True)
