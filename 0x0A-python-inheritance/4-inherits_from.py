#!/usr/bin/python3
'''
Only sub class of
'''


def inherits_from(obj, a_class):
    """
    Return True if the object is an instance of a class that
    inherited (directly or indirectly) from the specified class;
    otherwise, False.

    Prototype:
        def inherits_from(obj, a_class):

    Args:
        obj: The object to check.
        a_class: The specified class to compare against.

    Returns:
        bool: True if the object is an instance of a class that inherited
        from the specified class; False otherwise.
    """
    return type(obj) is not a_class and issubclass(type(obj), a_class)
