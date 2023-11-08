#!/usr/bin/python3

def search_replace(my_list, search, replace):
    dup = my_list.copy()
    position = []
    a = 0
    for i in my_list:
        if i == search:
            position.append(a)
        a += 1
    for b in position:
        dup[b] = replace

    return dup
