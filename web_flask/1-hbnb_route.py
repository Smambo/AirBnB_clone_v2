#!/usr/bin/python3
"""Import module to start Flask"""
from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    """Displays string of characters"""
    return ("Hello HBNB!")


@app.route('/hbnb')
def hbnb():
    """Displays HBNB text"""
    return ("HBNB")


if __name__ == "__main__":
    app.url_map.strict_slashes=False
    app.run(host="0.0.0.0.", port=5000)
