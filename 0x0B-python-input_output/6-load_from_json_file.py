#!/usr/bin/python3
"""
Save Object to a file
"""
import json


def load_from_json_file(filename):
    """
    A function that creates an Object from a “JSON file”

    Prototype:
        def load_from_json_file(filename):

    Args:
        filename (str): The name of the JSON file
    """
    with open(filename, 'r', encoding='utf-8') as f:
        return json.loads(f.read())
