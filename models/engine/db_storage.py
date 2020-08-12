#!/usr/bin/python3
""" This module defines a class to manage DataBase for hbnb clone"""
from os import getenv
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine


class DBStorage():
    """ This class manages DataBase of hbnb models in MySQL"""
    __engine = None
    __session = None

    def __init__(self):
        """Constructor"""
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.format
                        (getenv(HBNB_MYSQL_USER),
                        getenv(HBNB_MYSQL_PWD),
                        getenv(HBNB_MYSQL_HOST),
                        getenv(HBNB_MYSQL_DB)), pool_pre_ping=True)
        if getenv(HBNB_ENV) is 'test':
            Base.metadata.drop_all(self.__engine)
        Base.metadata.create_all(self.__engine)
        Session = sessionmaker(bind=self.__engine)
        self.__session = Session()

    def all(self, cls=None):
        """Query on the current database session all objects depending
        of the class name"""

        if cls in None:
            classes = [User, State, City, Amenity, Place, Review]
            for clase in classes:
                result = self.__session.query(clase).all()
                dic = {}
                for element in result:
                    key = "{}.{}".format(clase.__name__, element.id)
                    dic[key] = element
            return dic
        else:
            result = self.__session.query(cls).all()
            dic = {}
            for element in result:
                key = "{}.{}".format(cls.__name__, element.id)
                dic[key] = element
            return dic
