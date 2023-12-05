#!/usr/bin/python3
"""
Append to a file
"""


def append_write(filename="", text=""):
    '''
    A function that appends a string at the end of a text file (UTF8) and returns the number of characters added.
    
    Prototype:
        def append_write(filename="", text=""):
    
    Args:
        filename (str): The name of the file. Default is an empty string.
        text (str): The content to be appended to the file. Default is an empty string
    
    Returns:
        The number of characters added.'''
    with open(filename, 'a', encoding='utf-8') as f:
        num = f.append(text)
        return num