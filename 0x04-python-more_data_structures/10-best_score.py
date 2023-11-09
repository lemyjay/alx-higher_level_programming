#!/usr/bin/python3

def best_score(a_dictionary):
    if not a_dictionary:
        return None
    key_list = []
    for x, y in a_dictionary.items():
        key_list.append(x)
    key_list.sort()
    return key_list[-1]
