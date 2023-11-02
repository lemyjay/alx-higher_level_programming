#!/usr/bin/python3

if __name__ == "__main__":
    import sys
    number = -1 
    argument = sys.argv
    for i in argument:
        number += 1
    if number == 0 or number == 1:
        print("{} argument:".format(number))
    else:
        print("{} arguments:".format(number))
    for a in range(1, number + 1):
        print("{}: {}".format(a, argument[a]))
