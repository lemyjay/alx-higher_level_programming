#!/usr/bin/python3
'''
Same class or inherit from
'''


def is_kind_of_class(obj, a_class):
    """
    Return True if the object is an instance of, or if the object is an instance of a class that inherited from,
    the specified class; otherwise, return False.

    Prototype:
        def is_kind_of_class(obj, a_class)

    Args:
        obj: The object to check.
        a_class: The specified class to compare against.

    Returns:
        bool: True if the object is an instance of, or inherited from, the specified class; False otherwise.
    """
    return type(obj) is (a_class, type(a_class))