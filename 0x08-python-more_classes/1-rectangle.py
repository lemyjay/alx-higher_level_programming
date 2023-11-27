#!/usr/bin/python3

'''An empty class Rectangle that defines a rectangle.'''


class Rectangle:
    '''A class for creating/defining a rectangle.'''

    def __init__(self, width=0, height=0):
        '''
        The initialization method for the class

        Args:
            width(int): the width of the rectangle.
            height(int): the height of the rectangle
        '''
        self.__width = width
        self.__height = height

    @property
    def width(self):
        '''The getter method for retrieving the width'''
        return self.__width

    @width.setter
    def width(self, value):
        '''
        The setter method for assigning a value to the width

        Args:
            value(int): value to be assigned to the width, hopefully an int
        '''
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        '''The getter method for retrieving the height'''
        return self.__height

    @height.setter
    def height(self, value):
        '''
        The setter method for assigning a value to the height

        Args:
            value(int): value to be assigned to the height, hopefully an int
        '''
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value
