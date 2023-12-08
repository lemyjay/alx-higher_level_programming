#!/usr/bin/python3
"""
Base class
"""


class Base:
    """
    The Base class is the foundation for all other classes in this project.
    It manages the 'id' attribute, ensuring its proper assignment based on the provided argument.

    Attributes:
        __nb_objects (int): A private class attribute to keep track of the number of objects created.

    Methods:
        __init__(self, id=None): The class constructor.
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        The class constructor.

        If 'id' is not None, assign it to the public instance attribute 'id'.
        Otherwise, increment __nb_objects and assign the new value to 'id'.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
