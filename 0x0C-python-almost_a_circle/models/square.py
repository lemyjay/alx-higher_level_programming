#!/usr/bin/python3
"""
Square class that inherits from the Rectangle class
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """
    Square class, inherits from Rectangle.

    Attributes:
        id (int): Unique identifier for each square.
        size (int): Size of the square.
        x (int): X-coordinate of the square.
        y (int): Y-coordinate of the square.

    Methods:
        __init__(self, size, x=0, y=0, id=None): Constructor for Square.

        __str__(self): Overrides the __str__ method to return a string
        representation of the Square.
    """
    def __init__(self, size, x=0, y=0, id=None):
        """
        Constructor for Square.

        Args:
            size (int): Size of the square.
            x (int): X-coordinate of the square. Defaults to 0.
            y (int): Y-coordinate of the square. Defaults to 0.
            id (int): Unique identifier for the square. Defaults to None.
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """
        Overrides the __str__ method to return a string representation
        of the Square.

        Returns:
            str: A string representation of the Square in the format:
            [Square] (<id>) <x>/<y> - <size>
        """
        return "[{}] ({}) {}/{} - {}".format(
                self.__class__.__name__,
                self.id, self.x, self.y,
                self.width
                )

    @property
    def size(self):
        """Get or set the size of the square.

        Returns:
            int: The size of the square, which is both the width and height.

        Notes:
            The size is determined by the width and height attributes, as they are
            always equal in a square.
        """
        return self.width

    @size.setter
    def size(self, value):
        """Set the size of the square.

        Args:
            value (int): The new size to set for both width and height.
        """
        self.width = value
        self.height = value
