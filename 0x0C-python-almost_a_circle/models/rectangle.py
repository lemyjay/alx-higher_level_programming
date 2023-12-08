#!/usr/bin/python3
"""
Rectangle class that inherits from Base
"""
from models.base import Base


class Rectangle(Base):
    """
    Rectangle class, inherits from Base.

    Private instance attributes:
        __width (int): Width of the rectangle.
        __height (int): Height of the rectangle.
        __x (int): X-coordinate of the rectangle.
        __y (int): Y-coordinate of the rectangle.

    Attributes:
        id (int): Unique identifier for each rectangle.

    Methods:
        __init__(self, width, height, x=0, y=0, id=None): Constructor for
        Rectangle.
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Constructor for Rectangle.

        Args:
            width (int): Width of the rectangle.
            height (int): Height of the rectangle.
            x (int): X-coordinate of the rectangle. Defaults to 0.
            y (int): Y-coordinate of the rectangle. Defaults to 0.
            id (int): Unique identifier for the rectangle. Defaults to None.
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """The getter method for retreiving the width"""
        return self.__width

    @width.setter
    def width(self, value):
        """
        The setter method for assigning a value to the width

        Args:
            value (int): value to be assigned to the width, hopefully an int
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if (value <= 0):
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """The getter method for retreiving the height"""
        return self.__height

    @height.setter
    def height(self, value):
        """
        The setter method for assigning a value to the height

        Args:
            value (int): value to be assigned to the height, hopefully an int
        """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if (value <= 0):
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """The getter method for retreiving the value of x"""
        return self.__x

    @x.setter
    def x(self, value):
        """
        The setter method for assigning a value to x

        Args:
            value (int): value to be assigned to x, hopefully an int
        """
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if (value < 0):
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """The getter method for retreiving the value of y"""
        return self.__y

    @y.setter
    def y(self, value):
        """
        The setter method for assigning a value to y

        Args:
            value (int): value to be assigned to the y, hopefully an int
        """
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if (value < 0):
            raise ValueError("y must be >= 0")
        self.__y = value
    
    def area(self):
        """
        Returns the area value of the Rectangle instance.

        Returns:
            int: The area of the rectangle.
        """
        return self.__height * self.__width
    
    def display(self):
        """
        Prints in stdout the Rectangle instance with the character '#'.
        """
        for _ in range(self.__height):
            print("#" * self.__width)