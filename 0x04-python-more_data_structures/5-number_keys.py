#!/usr/bin/python3
def number_keys(a_dictionary):
    """
    returns the number of keys in a dictionary.

    Args:
        a_dictionary (dict): dictionary

    Return:
        the number of keys in a dictionary.
    """
    count = 0
    for key in a_dictionary:
        count += 1

    return count
