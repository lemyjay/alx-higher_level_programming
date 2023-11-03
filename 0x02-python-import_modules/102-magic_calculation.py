#!/usr/bin/python3
def magic_calculation(a, b):
    from magic_calculation_102 import add, sub
    if a < b:
        return add(a, b)
    else:
        return sub(a, b)
