#!/usr/bin/python3
"""Starts a flask web application"""
from flask import Flask, render_template

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/', strict_slashes=False)
def home():
    """"""
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """"""
    return 'HBNB'


@app.route('/c/<text>')
def c_params(text):
    """"""
    text_new = text.replace('_', ' ')

    return "C {}".format(text_new)


@app.route('/python', defaults={'text': 'is_cool'})
@app.route('/python/<text>')
def p_params(text):
    """"""
    text_new = text.replace('_', ' ')

    return "Python {}".format(text_new)


@app.route('/number/<int:n>')
def number(n):
    """"""
    return "{} is a number".format(n)


@app.route('/number_template/<int:n>')
def numtemp(n):
    """"""
    return render_template('5-number.html', number=n)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
