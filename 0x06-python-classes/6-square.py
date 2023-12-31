#!/usr/bin/python3
''' Defines a square. '''


class Square:
    ''' A class that defines a square. '''

    def __init__(self, size=0, position=(0, 0)):
        '''
        The __init__ method with private attributes: size and postion.

        Args:
            size(int): the size of the square
            position(tuple): a tuple of two posible integers
        '''
        self.size = size
        self.position = position

    @property
    def position(self):
        ''' Getter method to retrieve the position attribute. '''
        return self.__position

    @position.setter
    def position(self, value):
        '''
        Setter method to set the position attribute.

        Args:
            value(tuple): the position values to be set
        '''
        if (not isinstance(value, tuple) or len(value) != 2 or not
                all(isinstance(i, int) for i in value) or not
                all(i >= 0 for i in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

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

    def area(self):
        ''' Computes the area of the square and returns the result. '''
        return self.__size ** 2

    def my_print(self):
        '''
        Prints in stdout the square with the character #. If the size
        equals 0, an empty line is printed.
        '''
        if self.__size == 0:
            print()
        else:
            for a in range(self.__position[1]):
                print()
            for b in range(self.__size):
                print(" " * self.__position[0] + "#" * self.__size)
