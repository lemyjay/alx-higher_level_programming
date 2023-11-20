#!/usr/bin/python3

def _len(my_list=[]):
    b = 0
    for c in my_list:
        b += 1
    return b

def safe_print_list_integers(my_list=[], x=0):
    try:
        k = 0
        for a in range(x):
            if isinstance(my_list[a], int):
                print("{:d}".format(my_list[a]), end="")
                k += 1
        print()
        return k
    except TypeError as e:
        print(e)
    except IndexError as e:
        print(e)
    except ValueError as e:
        print(e)
