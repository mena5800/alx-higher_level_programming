#!/usr/bin/python3

"""
this module has only one function is_same_class
"""


def is_same_class(obj, a_class):
    """
    returns True if the object is exactly an instance of
    the specified class ; otherwise False.

    Arguemnts:
        obj : the object to check
                a_class : the class
        Return:
                true if obj and a_class is the same class otherwise false.
    """
    if type(obj) is a_class:
        return True
    else:
        return False
