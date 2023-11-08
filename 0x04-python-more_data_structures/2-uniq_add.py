#!/usr/bin/python3

def uniq_add(my_list=[]):
    dup = set()
    total = 0

    for num in my_list:
        if num not in dup:
            total += num
            dup.add(num)

    return total
