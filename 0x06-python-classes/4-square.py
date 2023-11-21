#!/usr/bin/python3
''' Defines a square. '''


class Square:
    ''' A class that defines a square. '''
    def __init__(self, size=0):
        '''
        The __init__ method with a private size attribute.

        Args:
            size(int): the size of the square
        '''
        self.__size = size

    def area(self):
        ''' Computes the area of the square and returns the result. '''
        return self.__size ** 2

    @property
    def size(self):
        ''' Getter method to retrieve the size attribute. '''
        return self.__size

    @size.setter
    def size(self, value):
        '''
        Setter method to set the size attribute.

        Args:
            value(int): the size value to be set
        '''
        if type(value) != int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
