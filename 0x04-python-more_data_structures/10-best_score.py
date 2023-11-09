#!/usr/bin/python3

def best_score(a_dictionary):
    if not a_dictionary:
        return None
    key_list = []
    if len(list(a_dictionary.items())) == 1:
        a, b = a_dictionary.items()
        return b
    elif len(list(a_dictionary.items())) == 0:
        return 0
    for x, y in a_dictionary.items():
        key_list.append(x)
    key_list.sort()
    return key_list[-1]
