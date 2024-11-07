#!/usr/bin/env python3
"""
A basic Flask app
"""


from flask import Flask, render_template, request
from flask_babel import Babel


class Config():
    """
    Class perfroms babel configurations at instatiation.
    """

    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"

    LANGUAGES = ["en", "fr"]


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)


@app.route('/')
def home():
    """
    Route to home page.
    """
    return render_template('2-index.html')


@babel.localeselector
def get_locale():
    """
    Selects best locale based on user request.
    """
    return request.accept_languages.best_match(app.config['LANGUAGES'])


if __name__ == "__main__":
    app.run()  # debug=True#)
