#!/usr/bin/python3
def uppercase(str):
    for char in str:
        char_ord = ord(char)
        if (char_ord >= ord('a')) and (char_ord <= ord('z')):
            char = chr(char_ord - ord('a') + ord('A'))
        print("{}".format(char), end='')
    print()
