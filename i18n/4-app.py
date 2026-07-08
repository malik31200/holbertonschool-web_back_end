#!/usr/bin/env python3
"""
Basic Flask app with Babel selection.
"""

from flask import Flask, render_template, request
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


def get_locale():
    """Determine the best language match"""
    locale = request.args.get("locale")

    if locale and locale in app.config["LANGUAGES"]:
        return locale
    return request.accept_languages.best_match(app.config["LANGUAGES"])


babel.init_app(app, locale_selector=get_locale)


@app.route('/')
def index() -> str:
    """
    Display the home page
    """
    return render_template("3-index.html")


if __name__ == "__main__":
    app.run(debug=True)
