#!/usr/bin/python3
"""
Save Object to a file
"""
import json


def save_to_json_file(my_obj, filename):
    """
    A function that writes an Object to a text file, using a JSON
    representation

    Prototype:
        def save_to_json_file(my_obj, filename):

    Args:
        my_obj: The object to be serialized to a JSON-formatted string.
        filename (str): The name of the file
    """
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(json.dumps(my_obj))
