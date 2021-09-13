#!/usr/bin/python3
""" Review module for the HBNB project """
from models.base_model import Base, BaseModel


class Review(BaseModel, Base):
    """ Review class to store review information """
    __tablename__ = "reviews"
    place_id = ""
    user_id = ""
    text = ""
