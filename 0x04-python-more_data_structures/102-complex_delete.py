#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    """
    deletes keys with a specific value in a dictionary.

    Args:
        a_dictionary (_type_): _description_
        value (_type_): _description_
    """
    if (a_dictionary is None or value is None):
        return a_dictionary
    my_list = []
    for key in a_dictionary:
        if (a_dictionary[key] == value):
            my_list.append(key)

    for key in my_list:
        a_dictionary.pop(key)

    return a_dictionary
