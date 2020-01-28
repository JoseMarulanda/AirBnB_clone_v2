#!/usr/bin/python3
"""script that starts a Flask web application"""

from flask import Flask, render_template

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """ Display Hello HBNB """
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """ Display HBNB """
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def c_text(text):
    """Display C and a text"""
    return 'C %s' % text.replace('_', ' ')


@app.route('/python/', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def py_text(text='is cool'):
    """Display Python and a text"""
    if text is not 'is cool':
        text = text.replace('_', ' ')
    return 'python %s' % text


@app.route('/number/<int:n>', strict_slashes=False)
def num(n):
    """Display a number"""
    return '%d is a number' % n


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    """Display a html page"""
    return render_template('5-number.html', number=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def number_odd_or_even(n):
    """ Display a html page """
    return render_template('6-number_odd_or_even.html', number=n)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
