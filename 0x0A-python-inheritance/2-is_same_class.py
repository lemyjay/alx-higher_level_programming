#!/usr/bin/python3
'''
Exact same object
'''


def is_same_class(obj, a_class):
    """
    Return True if the object is exactly an instance of the specified class; otherwise, return False.

    Prototype:
        def is_same_class(obj, a_class):

    Args:
        obj: The object to check.
        a_class: The specified class to compare against.

    Returns:
        bool: True if the object is exactly an instance of the specified class; False otherwise.
    """
    return type(obj) is a_class
