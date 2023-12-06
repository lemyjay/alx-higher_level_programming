#!/usr/bin/python3
'''
Can I?
'''


def add_attribute(obj, attribute, value):
    """
    Adds a new attribute to an object if it's possible.

    Args:
        obj: The object to which the new attribute should be added.
        attribute (str): The name of the new attribute.
        value: The value of the new attribute.

    Raises:
        TypeError: If the object cannot have a new attribute.

    Note:
        This function does not use try/except and does not import any module.
    """
    if "__dict__" not in dir(obj):
        raise TypeError("can't add new attribute")
    setattr(obj, attribute, value)
    