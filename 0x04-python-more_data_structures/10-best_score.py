#!/usr/bin/python3
def best_score(a_dictionary):
    """
    returns a key with the biggest integer value.

    Args:
        a_dictionary (dict): initial dict
    """
    if (a_dictionary is None):
        return None
    max_value = -float("inf")
    key_max_value = None
    for key in a_dictionary:
        if (max_value < a_dictionary[key]):
            key_max_value = key
            max_value = a_dictionary[key]
    return key_max_value
