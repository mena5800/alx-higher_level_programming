#!/usr/bin/python3
"""
this module has only one function
"""


def is_kind_of_class(obj, a_class):
    """
    returns True if the object is an instance of, or if the object is
    an instance of a class that inherited from,
    the specified class ; otherwise False.

    Arguments:
                obj : the object we want to ckeck
                a_class : the class

        Return:
                True: if the same class
                False: otherwise
    """
    return isinstance(obj, a_class)
