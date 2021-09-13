#!/usr/bin/python3
""" This module defines a class to manage database sql """
from os import getenv, environ
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from models.base_model import Base
from models.user import User
from models.state import State
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.city import City

class DBStorage:
    """ database mysql object """
    __engine = None
    __session = None

    def __init__(self):
        """ Initializes MySqlalchemy engine with env parameters """

        mysqlUser = getenv('HBNB_MYSQL_USER')
        mysqlPass = getenv('HBNB_MYSQL_PWD')
        mysqlHost = getenv('HBNB_MYSQL_HOST')
        mysqlDB = getenv('HBNB_MYSQL_DB')

        eng = "mysql+mysqldb://{}:{}@{}:3306/{}".\
            format(mysqlUser, mysqlPass, mysqlHost, mysqlDB)
        self.__engine = create_engine(eng, pool_pre_ping=True)

        if getenv('HBNB_ENV') == "test":
            Base.metadata.drop_all(bind=self.__engine)
    
    def all(self, cls=None):
        """ Returns all currect cls objects on db - cls=None returns all """
        if cls:
            queryArr = self.__session.query(cls).all()
        else:
            queryArr = []
            classes = ['State', 'User', 'Place', 'City', 'Review', 'Amenity']
            for _class in classes:
                objs = self.__session.query(_class)
                for obj in objs:
                    queryArr.append(obj)

        for obj in queryArr:
            key = type(obj).__name__ + "." + str(obj.id)
            queryDict = dict(key, obj)
        
        return queryDict

    def new(self, obj):
        """ Adds <obj> to current session """
        self.__session.add(obj)
    
    def save(self):
        """ Save/Commit current changes maded on sessions """
        self.__session.commit()
    
    def delete(self, obj=None):
        """ Deletes obj on session """
        if obj:
            self.__session.delete(obj)
    
    def reload(self):
        """ Recreates a new metadata from DB """
        Base.metadata.create_all(self.__engine)
        Session = sessionmaker(bind=self.__engine, expire_on_commit=False)
        self.__session = scoped_session(Session)()
