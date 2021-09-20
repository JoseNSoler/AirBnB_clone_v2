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

        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'
                                      .format(mysqlUser,
                                              mysqlPass,
                                              mysqlHost,
                                              mysqlDB), pool_pre_ping=True)

        if getenv('HBNB_ENV') == "test":
            Base.metadata.drop_all(bind=self.__engine)

        self.__session = sessionmaker(bind=self.__engine)

    def all(self, cls=None):
        """ Returns all currect cls objects on db - cls=None returns all """
        queryDict = {}
        if cls:
            queryArr = self.__session.query(cls).all()

        else:
            queryArr = []
            queryArr += self.__session.query(State).all()
            queryArr += self.__session.query(City).all()
            queryArr += self.__session.query(User).all()
            queryArr += self.__session.query(Place).all()
            queryArr += self.__session.query(Amenity).all()
            queryArr += self.__session.query(Review).all()

        for objects in queryArr:
            key = type(objects).__name__ + "." + str(objects.id)
            queryDict[key] = objects
        return queryDict

    def new(self, obj):
        """ Adds <obj> to current session """
        return self.__session.add(obj)

    def save(self):
        """ Save/Commit current changes maded on sessions """
        return self.__session.commit()

    def delete(self, obj=None):
        """ Deletes obj on session """
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """ Recreates a new metadata from DB """
        Base.metadata.create_all(self.__engine)
        Session = sessionmaker(bind=self.__engine, expire_on_commit=False)
        self.__session = scoped_session(Session)()

    def close(self):
        """ Removes current session from current thread """
        self.__session.close()
