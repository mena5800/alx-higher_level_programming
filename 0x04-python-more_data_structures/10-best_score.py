#!/usr/bin/python3
def best_score(a_dictionary):
    """
    returns a key with the biggest integer value.

    Args:
        a_dictionary (dict): initial dict
    """
    if (a_dictionary == None):
        return None
    max_value = max(list(a_dictionary.values()))
    return max_value
