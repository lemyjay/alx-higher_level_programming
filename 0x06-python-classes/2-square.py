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
        if type(size) != int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
