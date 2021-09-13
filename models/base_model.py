#!/usr/bin/python3
"""This module defines a base class for all models in our hbnb clone"""
from os import getenv
import models
import uuid
from datetime import datetime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Table, Column, MetaData , String, DateTime

if getenv("HBNB_TYPE_STORAGE") == "db":
    Base = declarative_base()
    metadata = MetaData()
else:
    Base = object


class BaseModel:
    """A base class for all hbnb models"""

    id = Column(String(60),
                nullable=False,
                primary_key=True)
    
    created_at = Column(DateTime,
                nullable=False,
                default=datetime.utcnow())
    
    updated_at = Column(DateTime,
                nullable=False,
                default=datetime.utcnow())


    def __init__(self, *args, **kwargs):
        """Instatntiates a new model"""
        storage_system = getenv('HBNB_TYPE_STORAGE')
        if kwargs:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                if key != "__class__":
                    if storage_system == 'db':
                        value = value.strip('"')
                    setattr(self, key, value)
            if self.id is None:
                setattr(self, 'id', str(uuid.uuid4()))
        else:
            self.id = str(uuid.uuid4())
            self.created_at = self.updated_at = datetime.now()

    def __str__(self):
        """Returns a string representation of the instance"""
        string = "[{}] ({}) {}".format(
            self.__class__.__name__,
            self.id,
            str(self.to_dict()))
        return string
    
    def __repr__(self):
        """ Returns a string representaion """
        return self.__str__()

    def save(self):
        """Updates updated_at with current time when instance is changed"""
        self.updated_at = datetime.now()
        models.storage.new(self)
        models.storage.save()

    def to_dict(self):
        """Convert instance into dict format"""
        dicto = dict(self.__dict__)
        if "_sa_instance_state" in dicto.keys(): del dicto["_sa_instance_state"]
        dicto["__class__"] = str(type(self).__name__)
        dicto['created_at'] = self.created_at.isoformat()
        dicto['updated_at'] = self.updated_at.isoformat()
        return dicto
    
    def delete(self):
        models.storage.delete(self)
