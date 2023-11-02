#!/usr/bin/python3

if __name__ == "__main__":
    import sys

    number = len(sys.argv) - 1
    arguments = sys.argv

    if number == 1:
        print("{} argument:".format(number))
    else:
        print("{} arguments:".format(number))
    for a in range(1, number + 1):
        print("{}: {}".format(a, arguments[a]))
