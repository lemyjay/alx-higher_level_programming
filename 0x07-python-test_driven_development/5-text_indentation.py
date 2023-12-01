#!/usr/bin/python3
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

    string = ""
    indicators = [".", "?", ":"]
    prev = ""
    start = True
    for i in text:
        if i == " " and start:
            continue
        else:
            start = False
            if i in indicators:
                string += i
                string += "\n\n"
                prev = "\n"
            else:
                if prev == "\n" and i == " ":
                    continue
                else:
                    string += i
                    prev = ""

    print(string, end="")
