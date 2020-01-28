#!/usr/bin/python3
"""script that starts a Flask web application"""

from flask import Flask

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
        
if __name__=='__main__':
    app.run(host='0.0.0.0', port=5000)