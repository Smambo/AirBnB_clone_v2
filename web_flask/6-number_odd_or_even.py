#!/usr/bin/python3
"""Import module for Flask."""
from flask import Flask
from flask import abort
from flask import render_template

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


@app.route('/python/', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_text(text="is cool"):
    """Displays 'Python' followed by value of 'text'."""
    return ("Python " + text.replace("_", ' '))


@app.route('/number/<n>', strict_slashes=False)
def number(n):
    """Displays the value of n, which must be an int."""
    try:
        return ("{} is a number".format(int(n)))
    except:
        abort(404)


@app.route('/number_template/<n>', strict_slashes=False)
def number_template(n):
    """Displays html page if n is an int."""
    try:
        return (render_template('5-number.html', n=int(n)))
    except:
        abort(404)


@app.route('/number_odd_or_even/<n>', strict_slashes=False)
def number_odd_or_even(n):
    """Displays html page if n is an int. Even or odd."""
    try:
        return (render_template('6-number_odd_or_even.html', n=int(n)))
    except:
        abort(404)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
