#!/usr/bin/python3
"""
This module performs addition of two integers and sets the second to a
default value of 98
"""


def add_integer(a, b=98):
    """
    A funtion that adds 2 integers.

    Prototype:
    def add_integer(a, b=98)

    Args:
        a (int or float): the first integer
        b (int or float, default: 98): the second integer

    Returns:
        int: The sum of the two integers

    Raises:
        TypeError: if a or b is not an integer or a float.
    """
    if not isinstance(a, (float, int)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (float, int)):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
