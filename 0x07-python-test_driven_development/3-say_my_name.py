#!/usr/bin/python3
"""
Say my name
"""


def say_my_name(first_name, last_name=""):
    '''
    A function that prints: My name is <first name> <last name>

    Prototype:
        def say_my_name(first_name, last_name=""):

    Args:
        first_name (string): the first name
        last_name (string): the last name, default is an empty string

    Raises:
        TypeError: if last_name or first_name is not a string
    '''
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
