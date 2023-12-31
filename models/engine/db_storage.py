#!/usr/bin/python3
"""this module defines a class to manage db storage for hbnb clone"""
from sqlalchemy import create_engine
import os
from sqlalchemy.orm import sessionmaker, scoped_session, relationship
from models.base_model import Base, BaseModel
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User


class DBStorage:
    """This class manages storage of hbnb models in using SQL"""

    __engine = None
    __session = None

    def __init__(self):
        """handles initialization"""
        user = os.getenv('HBNB_MYSQL_USER')
        password = os.getenv('HBNB_MYSQL_PWD')
        host = os.getenv('HBNB_MYSQL_HOST', default='localhost')
        db = os.getenv('HBNB_MYSQL_DB')
        self.__engine = create_engine(
                f'mysql+mysqldb://{user}:{password}@{host}/{db}',
                pool_pre_ping=True
                )

        if os.getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """Returns a dictionary of models currently in storage"""
        if cls is None:
            objects = self.__session.query(State).all()
            objects.extend(self.__session.query(City).all())
            objects.extend(self.__session.query(Amenity).all())
            objects.extend(self.__session.query(Place).all())
            objects.extend(self.__session.query(Review).all())
            objects.extend(self.__session.query(User).all())
        else:
            if type(cls) == str:
                cls = eval(cls)
            objects = self.__session.query(cls)
        obj_dict = {f"{type(obj).__name__}.{obj.id}": obj for obj in objects}
        return obj_dict

    def new(self, obj):
        """Adds new object to storage"""
        if obj:
            session = self.__session()
            session.add(obj)

    def save(self):
        """Saves storage to Database"""
        session = self.__session()
        session.commit()

    def delete(self, obj=None):
        """Deletes object from Database"""
        if obj:
            session = self.__session()
            session.delete(obj)

    def reload(self):
        """Loads storage dictionary from Database"""
        models.base_model.Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(
                bind=self.__engine,
                expire_on_commit=False
                )
        self.__session = scoped_session(session_factory)

    def close(self):
        """Closes SQLAlchemy session"""
        self.__session.close()
