#!/usr/bin/python3
""" Start flask app """

from flask import Flask, escape, render_template
from models.state import State
from models.city import City
from models import storage
from os import getenv

app = Flask('__name__')

app.url_map.strict_slashes = False


@app.route('/cities_by_states')
def statesList():
    # Return string on root req
    states = storage.all(State).values()
    return render_template('8-cities_by_states.html', states=states)


@app.teardown_appcontext
def closeStorage(exception):
    # Return close session on
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
