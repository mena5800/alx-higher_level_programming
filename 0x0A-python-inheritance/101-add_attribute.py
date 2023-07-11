#!/usr/bin/python3
"""
this module contain function add_attribute
"""


def add_attribute(object, name, value):
    """
    this function try to add attribute to object
    """
    if not hasattr(object, "__dict__"):
        raise TypeError("can't add new attribute")
    else:
        setattr(type(object), name, value)
