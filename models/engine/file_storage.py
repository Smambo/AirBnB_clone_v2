#!/usr/bin/python3
"""This module defines a class to manage file storage for hbnb clone"""
import json
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


class FileStorage:
    """This class manages storage of hbnb models in JSON format"""
    __file_path = 'file.json'
    __objects = {}

    def all(self, cls=None):
        """Returns a dictionary of models currently in storage"""
        if cls is not None:
            if type(cls) == str:
                cls = eval(cls)
            new_dict = {}
            for key, value in self.__objects.items():
                if type(value) == cls:
                    new_dict[key] = value
            return (new_dict)
        return (self.__objects)

    def new(self, obj):
        """Adds new object to storage dictionary"""
        self.__objects["{}.{}".format(type(obj).__name__, obj.id)] = obj

    def save(self):
        """Saves storage dictionary to file"""
        temp = {o: self.__objects[o].to_dict() for o in self.__objects.keys()}
        with open(self.__file_path, 'w', encoding='utf-8') as f:
            json.dump(temp, f)

    def reload(self):
        """Loads storage dictionary from file"""
        try:
            with open(self.__file_path, 'r', encoding='utf-8') as f:
                for ob in json.load(f).values():
                    name = ob["__class__"]
                    del ob["__class__"]
                    self.new(eval(name)(**ob))
        except FileNotFoundError:
            pass

    def delete(self, obj=None):
        """Deletes object from __objects if it's inside"""
        try:
            del self.__objects["{}.{}".format(type(obj).__name__, obj.id)]
        except (AttributeError, KeyError):
            pass

    def close(self):
        """Calls the reload method"""
        self.reload()
