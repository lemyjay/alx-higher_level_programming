#!/usr/bin/python3

def multiply_by_2(a_dictionary):
    dup = a_dictionary.copy()
    for x, y in dup.items():
        dup[x] = y * 2
    return dup
