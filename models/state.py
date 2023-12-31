#!/usr/bin/python3
""" State Module for HBNB project """
import models
from models.base_model import BaseModel, Base
from models.city import City
from os import getenv
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)
    cities = relationship(
            "City",
            cascade="all, delete-orphan",
            backref="state"
            )

    if os.getenv("HBNB_TYPE_STORAGE") != "db":
        @property
        def cities(self):
            """gets list of city instances related to state instance"""
            city_ls = []
            all_cities = models.storage.all(City)
            for city in all_cities.values():
                if city.state_id == self.id:
                    city_ls.append(city)
            return city_ls
