#!/usr/bin/python3
"""
From JSON string to Object
"""
import json


def from_json_string(my_str):
    """
    A function that returns an object (Python data structure) represented by a JSON string

    Prototype:
        def from_json_string(my_str):

    Args:
        my_str: The JSON-formatted string to be deserialized.

    Returns:
        object: The Python data structure represented by the input JSON string.
    """
    return json.loads(my_str)
