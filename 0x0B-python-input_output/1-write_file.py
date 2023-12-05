#!/usr/bin/python3
"""
Write to a file
"""


def write_file(filename="", text=""):
    '''
    A function that writes a string to a text file (UTF8) and
    returns the number of characters written.
    
    Prototype:
        def write_file(filename="", text=""):
    
    Args:
        filename (str): The name of the file. Default is an empty string
        text (str): The content to be written to the file. Default is an empty string
    '''
    with open(filename, 'w', encoding='utf8') as f:
        f.write(text)
    with open(filename, 'r', encoding='utf8') as f:
        content = f.read()
        if content == text:
            return (len(text))