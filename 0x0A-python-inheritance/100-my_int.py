#!/usr/bin/python3
"""
this module contian class MyInt that inherits from int.
"""


class MyInt(int):
    """
    this class inherit from int
    """

    def __eq__(self, other):
        "this function to retrun opposite resutls"
        return super().__ne__(other)

    def __ne__(self, other):
        "this function to retrun opposite resutls"
        return super().__eq__(other)
