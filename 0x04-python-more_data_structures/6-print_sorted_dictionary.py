#!/usr/bin/python3

def print_sorted_dictionary(a_dictionary):
    key_list = []
    for x in a_dictionary.items():
        key_list.append(x)
    key_list.sort()
    for i in key_list:
        print("{}: {}".format(i[0], a_dictionary[i[0]]))
