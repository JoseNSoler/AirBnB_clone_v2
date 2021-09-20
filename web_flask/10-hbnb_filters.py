#!/usr/bin/python3
""" Start flask app """

from flask import Flask, escape, render_template
from models.state import State
from models.amenity import Amenity
from models import storage
from os import getenv

app = Flask('__name__')

app.url_map.strict_slashes = False


@app.route('/hbnb_filters')
def statesList():
    # Return string on root req
    states = sorted(list(storage.all(State).values()), key=lambda x: x.name)
    amenities = sorted(list(storage.all(Amenity).values()), key=lambda x: x.name)
    return render_template(
        '10-hbnb_filters.html',
        states=states,
        amenities=amenities
        )


@app.teardown_appcontext
def closeStorage(exception):
    # Return close session on
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
