#!/usr/bin/python3
""" Start flask app """
from flask import Flask, escape, render_template

app = Flask('__name__')

app.url_map.strict_slashes = False


@app.route('/')
def index():
    # Return string on root req
    return 'Hello HBNB!'


@app.route('/hbnb')
def hbnb():
    # Return string on /hbnb req
    return 'HBNB'


@app.route('/c/<text>')
def cme(text):
    # Return 'C <user_req>'
    text = text.replace('_', ' ')
    return 'C %s' % escape(text)


@app.route('/python/')
@app.route('/python/<text>')
def python(text="is cool"):
    # Return Python <user_req>
    text = text.replace('_', ' ')
    return 'Python %s' % escape(text)


@app.route('/number/<int:n>')
def isnumber(n):
    # Return if <user_req_int> is a int
    if int(n):
        return "{} is a number".format(n)


@app.route('/number_template/<int:n>')
def display_html_if_num(n):
    # Return webpage if <user_req_int> is a int
    return render_template('5-number.html', n=int(n))

@app.route('/number_odd_or_even/<int:n>')
def odd_or_even(n):
    if (n % 2 == 0):
        return render_template('6-number_odd_or_even.html',
            n=n, stat='even')
    else:
        return render_template('6-number_odd_or_even.html',
            n=n, stat='odd')


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
