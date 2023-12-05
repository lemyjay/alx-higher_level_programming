#!/usr/bin/python3
"""
Read file
"""


def read_file(filename=""):
    """
    A function that reads a text file(UTF8) and prints it to stdout
    
    Prototype:
        def read_file(filename=""):
    
    Args:
        filename (str): The name of the file. Default is an empty string
    """
    with open(filename, 'r', encoding="utf8") as f:
        content = f.read()
        print(content)