#!/usr/bin/python3

if __name__ == "__main__":
    import sys
    arguments = sys.argv
    number = len(sys.argv)
    total = 0
    if number == 1:
        print(total)
    else:
        for i in range(1, len(sys.argv)):
            total += int(arguments[i])
        print(total)
