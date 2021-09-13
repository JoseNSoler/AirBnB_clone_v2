#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import Base, BaseModel


class Amenity(BaseModel, Base):
    __tablename__ = "amenities"
    name = ""
