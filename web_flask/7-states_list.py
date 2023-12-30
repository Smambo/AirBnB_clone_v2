#!/usr/bin/python3
"""Import modules for Flask web app"""
from models import storage
from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route('states_list', strict_slashes=False)
def states_list():
    """Displays HTML page"""
    return (render_template('7-states_list.html',
            storage=storage.all('State')))


@app.teardown_appcontext
def teardown(exception):
    """Removes SQLAlchemy session"""
    storage.close()


if __name__ == "__main__":
    app.run("0.0.0.0", port=5000)
