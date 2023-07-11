#!/usr/bin/python3
"""
this module has only one class
"""


class MyList(list):
    """
    class MyList inhert from list class
    """

    def print_sorted(self):
        """
        funciton to print list in sorted order
        """
        print(sorted(self))
