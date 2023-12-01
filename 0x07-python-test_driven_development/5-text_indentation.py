#!/usr/bin/python
"""
Text Indentation
"""


def text_indentation(text):
    """
    A function that prints a text with 2 new lines after each of these
    characters: ., ? and :

    Prototype:
        def text_indentation(text):

    Args:
        text (str): the text to be printed

    Raises:
        TypeError: if text is not a string
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    new_line = False
    for i in text:
        if i == "." or i == "?" or i == ":":
            print(i)
            new_line = True
        else:
            if new_line and i == " ":
                new_line = False
            else:
                print(i, end="")
