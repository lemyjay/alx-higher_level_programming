#!/usr/bin/python3
'''
Module that contains the class definition of a City.
'''


from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from model_state import Base


class City(Base):
    """
    Class that inherits from Base to link to the MySQL table cities.

    Attributes:
        - id: An auto-generated unique integer identifier for the city.
        - name: A string representing the name of the city, maximum length of 128 characters.
        - state_id: An integer representing the foreign key to states.id.
        - state: A relationship attribute, representing the State object linked to this city.
    """
    __tablename__ = 'cities'
    id = Column(
            Integer, primary_key=True,
            autoincrement=True, nullable=False
            )
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
    state = relationship("State", back_populates="cities")
