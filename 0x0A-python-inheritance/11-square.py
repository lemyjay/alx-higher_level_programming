#!/usr/bin/python3
'''
Square #2
'''
Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """
    A class representing a square, inheriting from Rectangle.

    Attributes:
        __size (int): The size of the square.
    """
    def __init__(self, size):
        """
        Initializes a Square instance.

        Args:
            size (int): The size of the square.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than or equal to 0.
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def __str__(self):
        """
        Returns a string representation of the square.

        Returns:
            str: A string in the format "[Square] <width>/<height>".
        """
        return "[Square] {}/{}".format(self.__size, self.__size)
