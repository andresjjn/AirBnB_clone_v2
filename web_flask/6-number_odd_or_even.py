#!/usr/bin/python3
""" Script that starts a Flask web application """
from flask import Flask, render_template
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """Hello funtion"""
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hello_():
    """HBNB funtion"""
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def c_ext(text):
    """ Return C + text passed like argument"""
    return "C %s" % text.replace('_', ' ')


@app.route('/python', defaults={'text': 'is cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_text(text):
    """ Display Python + is 'is cool' by default"""
    return "Python %s" % text.replace('_', ' ')


@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    """Display numbers passed like argument"""
    return "%d is a number" % n


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_2(n):
    """Display a HTML code with n into the body"""
    return render_template("5-number.html", number=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def number_3(n):
    """Display if n is an odd or even number"""
    return render_template("6-number_odd_or_even.html", number=n)

if __name__ == '__main__':
    app.run("0.0.0.0", 5000)
