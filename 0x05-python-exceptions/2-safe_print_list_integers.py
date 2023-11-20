#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    try:
        k = 0
        for a in range(x):
            if isinstance(my_list[a], int):
                print("{:d}".format(my_list[a]), end="")
                k += 1
        print()
        return k
    except (IndexError, TypeError):
        pass
