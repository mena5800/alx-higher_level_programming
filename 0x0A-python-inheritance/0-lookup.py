#!/usr/bin/python3

"""
this module has only one function lookup
"""


def lookup(obj):
    """
    returns the list of available attributes and methods of an object:
    """
    return (dir(obj))
