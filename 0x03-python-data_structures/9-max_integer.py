#!/usr/bin/python3

def max_integer(my_list=[]):
    if not my_list:
        return None
    result = 0
    for i in my_list:
        if int(i) > result:
            result = int(i)
    return result
