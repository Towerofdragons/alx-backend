#!/usr/bin/env python3
"""
A basic Flask app
"""


from flask import Flask, render_template
from flask_babel import Babel


class Config():
    """
    Class perfroms babel configurations at instatiation.
    """
   
    BABEL_DEFAULT_LOCALE= "en"
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
    return render_template('0-index.html', title="Welcome to Holberton", header="Hello world")


if __name__ == "__main__":
    app.run()  # debug=True#)
