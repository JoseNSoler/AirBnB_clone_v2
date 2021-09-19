#!/usr/bin/python3
""" Start flask app """
from flask import Flask, escape

app = Flask('__name__')


@app.route('/', strict_slashes=False)
def index():
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def cme(text):
    text = text.replace('_', ' ')
    return 'C %s' % escape(text)


@app.route('/python/', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python(text="is cool"):
    text = text.replace('_', ' ')
    return 'Python %s' % escape(text)


@app.route('/number/<n>', strict_slashes=False)
def isnumber(n):
    if int(n):
        return "{} is a number".format(n)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
