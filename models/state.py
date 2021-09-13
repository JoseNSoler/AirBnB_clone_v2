#!/usr/bin/python3
""" State Module for HBNB project """
from os import getenv, environ
import models
from models.base_model import Base, BaseModel
from models.city import City
from sqlalchemy import Table, Column, Integer , String, DateTime
from sqlalchemy.orm import relationship


class State(BaseModel, Base):
    """ State class """
    __tablename__ = "states"
    name = Column(String(128), nullable=False)

    if getenv('HBNB_TYPE_STORAGE') == 'db':
        cities = relationship("City", cascade="all")
    else:
        @property
        def cities(self):
            ''' returns the list of cities'''
            cities = models.storage.all(City)
            list_cities = []

            for city in cities.values():
                if city.state_id == self.id:
                    list_cities.append(city)
            return list_cities
