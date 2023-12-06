#!/usr/bin/python3
"""
Integer validator
"""


class BaseGeometry:
    """
    A class representing base geometry.

    Public Methods:
        def area(self): Raises an Exception with the message 'area() is not implemented.'
        def integer_validator(self, name, value): Validates the given value.

    Attributes:
        None
    """
    def area(self):
        """Raises an Exception with the message 'area() is not implemented.'"""
        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        """
        Validates the given value.

        Args:
            name (str): The name of the value.
            value: The value to be validated.

        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is less than or equal to 0.
        """
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
