#!/usr/bin/python3
for i in range(0, 26):
    char = ord('z') - i
    if i % 2 == 1:
        char = (chr(char - ord('a') + ord('A')))
    else:
        char = chr(char)
    print("{}".format(char), end='')
