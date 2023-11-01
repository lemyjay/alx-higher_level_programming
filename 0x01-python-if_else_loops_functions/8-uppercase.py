#!/usr/bin/python3

# A function that prints a string in uppercase followed by a new line.
def uppercase(str):
    result = ""
    for char in str:
        if 'a' <= char <= 'z':
            result += chr(ord(char) - 32)
        else:
            result += char
    print(result)
