#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    """
    deletes a key in a dictionary.

    Args:
        a_dictionary (dict): initial dict
        key (str, optional): key. Defaults to "".
    """
    if (a_dictionary.get(key, None) != None):
        a_dictionary.pop(key)

    return a_dictionary
