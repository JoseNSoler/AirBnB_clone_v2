#!/usr/bin/python3
""" City Module for HBNB project """
from sqlalchemy.orm import relationship
from sqlalchemy.sql.schema import ForeignKey
from models.base_model import Base, BaseModel
from sqlalchemy import Table, Column, Integer , String, DateTime

class City(BaseModel, Base):
    """ The city class, contains state ID and name """
    __tablename__ = "cities"
    name = Column(String(128), nullable=False)
    state_id = Column(String(60), ForeignKey("states.id"), nullable=False)
    places = relationship('Place', backref='cities', cascade='delete')
