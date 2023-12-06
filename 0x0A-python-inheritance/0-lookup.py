#!/usr/bin/python3
'''
Lookup
'''


def lookup(obj):
     """
    Return a list of available attributes and methods of an object.

    Prototype:
        def lookup(obj):

    Args:
        obj: The object for which to retrieve attributes and methods.

    Returns:
        list: A list containing the names of attributes and methods of the object.
    """
    return [attr for attr in dir(obj) if not callable(getattr(obj, attr)) or attr.startswith('__')]