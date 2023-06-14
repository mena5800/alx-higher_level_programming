#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    """
    replaces or adds key/value in a dictionary.

    Args:
        a_dictionary (dict): initial dictionary
        key (string): key 
        value (any type): value
    """
    a_dictionary[key] = value
    return a_dictionary
