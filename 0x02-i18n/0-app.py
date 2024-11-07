#!usr/bin/env python3
"""
A basic Flask app
"""


from flask import Flask, render_template
from flask_babel import Babel


class Config():
    """
    Class perfroms babel configurations at instatiation.
    """
    def __init__(self, babel):
        babel.default_locale = "en"
        babel.default_timezone = "UTC"

    LANGUAGES = ["en", "fr"]


app = Flask(__name__)
babel = Babel(app)
config = Config(babel)


@app.route('/')
def home():
    """
    Route to home page.
    """
    return render_template('0-index.html')


if __name__ == "__main__":
    app.run()  # debug=True#)
