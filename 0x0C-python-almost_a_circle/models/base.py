#!/usr/bin/python3
"""
Base class
"""
import json


class Base:
    """
    The Base class is the foundation for all other classes in this project.
    It manages the 'id' attribute, ensuring its proper assignment based on the
    provided argument.

    Attributes:
        __nb_objects (int): A private class attribute to keep track of the
                            number of objects created.

    Methods:
        __init__(self, id=None): The class constructor.

    Static Methods:
        to_json_string(list_dictionaries): Returns the JSON string
                                           representation of list_dictionaries.

        from_json_string(json_string): Converts a JSON string to a
                                        list of dictionaries.

    Class Methods:
        save_to_file(cls, list_objs): Save a list of instances to a JSON file.
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        The class constructor. Initializes a new instance of the Base class.

        Args:
            id (int): Identifier for the instance.

        Note:
            If 'id' is not None, assign to the public instance attribute 'id'.
            Otherwise, increment __nb_objects and assign the new value to 'id'.
        """

        if id is not None:
            if type(id) is not int:
                raise TypeError("id must be an integer")
            if id <= 0:
                raise ValueError("id must be greater than 0")
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Returns the JSON string representation of list_dictionaries.

        Args:
            list_dictionaries (list): A list of dictionaries.

        Returns:
            str: JSON string representation of list_dictionaries.
        """
        if list_dictionaries is None or not list_dictionaries:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @staticmethod
    def from_json_string(json_string):
        """
        Convert a JSON string to a list of dictionaries.

        Args:
            json_string (str): JSON string to be converted.

        Returns:
            list: List of dictionaries represented by the JSON string.
        """
        if json_string is None or json_string == "":
            return []
        return json.loads(json_string)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        Save a list of instances to a JSON file.

        Args:
            list_objs (list): List of instances to be saved.

        """
        filename = "{}.json".format(cls.__name__)
        with open(filename, "w") as file:
            if list_objs is None:
                file.write("[]")
            else:
                list_dicts = [obj.to_dictionary() for obj in list_objs]
                file.write(cls.to_json_string(list_dicts))
