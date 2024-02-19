#!/usr/bin/python3
'''
Module that defines the relationship of the state class
'''


from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from model_city import Base, City


class State(Base):
    """
    Class representing a state in a database.

    Attributes:
    - id: An auto-generated unique integer identifier for the state.
    - name: A string representing the name of the state, maximum
            length of 128 characters.
    """
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)
    cities = relationship("City", backref="state", cascade="all, delete")
