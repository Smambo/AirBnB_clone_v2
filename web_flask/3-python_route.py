#!/usr/bin/python3
"""Import module for Flask."""
from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """Displays string of characters"""
    return ("Hello HBNB!")


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """Displays HBNB text"""
    return ("HBNB")


@app.route('/c/<text>', strict_slashes=False)
def c(text):
    """Displays 'c' followed by value of 'text'."""
    return ("C " + text.replace("_", ' '))


@app.route('/python/')
@app.route('/python/<text>')
def python_text(text="is cool"):
    """Displays 'Python' followed by value of 'text'."""
    return ("Python " + text.replace("_", ' '))


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
