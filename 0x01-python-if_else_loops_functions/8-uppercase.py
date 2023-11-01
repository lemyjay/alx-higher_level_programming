# A function that prints a string in uppercase followed by a new line.
def uppercase(str):
    for char in str:
        if ord('a') <= ord(char) <= ord('z'):
            print("{}".format(chr(ord(char) - 32)), end="")
        else:
            print("{}".format(char), end="")
    print()  # Print a newline after the string
