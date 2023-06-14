#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    """
    prints a dictionary by ordered keys.

    Args:
        a_dictionary (dict): initial dictionary
    """
    my_list = list(a_dictionary.keys())
    my_list.sort()
    for key in my_list:
        print("{}: {}".format(key,a_dictionary[key]))
        
