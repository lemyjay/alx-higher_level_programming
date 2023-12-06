#!/usr/bin/python3
'''
My list
'''


class MyList(list):
    """
    A class that inherits from list.

    Public Methods:
        def print_sorted(self): Prints the list, but sorted in ascending order.

    Assumptions:
        - All elements of the list will be of type int.
    """
    def print_sorted(self):
        # Prints the list but in ascending order
        print(sorted(self))