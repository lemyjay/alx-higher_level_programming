#!/usr/bin/python3
''' Defines a square. '''


class Square:
    ''' A class that defines a square. '''
    def __init__(self, size):
        '''
        The __init__ method with a private size attribute.

        Args:
            size(int): the size of the square
        '''
        self.__size = size
