#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    try:
        i = 0
        for a in my_list:
            if i == x:
                break
            print("{}".format(a), end="")
            i += 1
        print()
        return i
    except Exception as e:
        print(e)
