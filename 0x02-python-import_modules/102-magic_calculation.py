#!/usr/bin/python3
def magic_calculation(a, b):
    if a < b:
        from magic_calculation_102 import add
        return add(a, b)
    else:
        from magic_calculation_102 import sub
        return sub(a, b)
