#!/usr/bin/python3
"""
To JSON string
"""
import json


def to_json_string(my_obj):
    """
    A function that returns the JSON representation of an object (string)

    Prototype:
        def to_json_string(my_obj):

    Args:
        my_obj: The object to be serialized to a JSON-formatted string.

    Returns:
        str: The JSON representation of an object (string)
    """
    return json.dumps(my_obj)
