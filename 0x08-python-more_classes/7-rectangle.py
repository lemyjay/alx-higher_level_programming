#!/usr/bin/python3

'''An empty class Rectangle that defines a rectangle.'''


class Rectangle:
    """
    Defines class rectangle with private attribute width and height

    Args:
        width (int): width
        height (int): height

    Attributes:
        number_of_instances (int): number of instances created and not deleted
        print_symbol (any type): used to print string representation

    Functions:
        __init__(self, width, height)
        width(self)
        width(self, value)
        height(self)
        height(self, value)
        area(self)
        perimeter(self)
        __str__(self)
        __repr__(self)
        __del__(self)
    """

    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        '''
        The initialization method for the class

        Args:
            width(int): the width of the rectangle.
            height(int): the height of the rectangle
        '''
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

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

    def area(self):
        '''
        The method for finding the area of the rectangle

        Return:
            The area of the rectangle
        '''
        return self.__width * self.__height

    def perimeter(self):
        '''
        The method for finding the perimeter of the rectangle

        Return:
            The perimeter of the rectangle
        '''
        if self.__width == 0 or self.__height == 0:
            return 0
        return (2 * self.__width) + (2 * self.__height)

    def __str__(self):
        '''
        Returns a string representation of the rectangle. In this case, with #

        Returns:
            A string of hashs(#) to represent the rectangle.
        '''
        if self.__width == 0 or self.__height == 0:
            return ""

        symbols = self.print_symbol
        if isinstance(symbols, list):
            symbols = repr(symbols)
        '''elif isinstance(symbols, (int, float)):
            symbols = str(symbols)'''

        string = ""
        for i in range(self.__height):
            string += str(symbols) * self.__width + "\n"
        return string[:-1]

    def __repr__(self):
        '''
        Returns a string representation of the rectangle to be able to recreate
        a new instance by using eval().

        Returns:
            A string that when passed to eval(), would create an equivalent
            instance of the rectangle.
        '''
        return f"Rectangle(width={self.__width}, height={self.__height})"

    def __del__(self):
        '''Deletes an instance of the class'''
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
