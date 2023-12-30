#!/usr/bin/python3
""" Script that runs an app with Flask framework """
from flask import Flask


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """ Function called with / route """
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """ Function called with /hbnb route """
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def c(text):
    """ Function called with /c/<text> route """
    return 'C {}'.format(text.replace('_', ' '))


@app.route('/python/', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_txt(text='is cool'):
    """ Function called with /python route """
    if text is not 'is cool':
        return 'Python {}'.format(text.replace('_', ' '))
    else:
        return 'Python {}'.format(text)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
