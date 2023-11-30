#!/usr/bin/python3
"""
Print square with #
"""


def print_square(size):
    """
    A function that prints a square with the character #

    Prototype:
        def print_square(size):

    Args:
        size (int): The size length of the square

    Raises:
        TypeError: if size is not an integer
                   if size is a float and less than 0
        ValueError: if size is less than 0
    """
    if not isinstance(size, (int, float)):
        raise TypeError("size must be an integer")
    if isinstance(size, int) and size < 0:
        raise ValueError("size must be >= 0")
    if isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")
    for i in range(int(size)):
        print("#" * int(size))
