#!/usr/bin/python3
def search_replace(my_list, search, replace):
    """
    replaces all occurrences of an element by another in a new list.

    Args:
        my_list (list): the initial list
        search (int): the element to replace in the list
        replace (int): is the new element

    Return:
        new_list (list): an updated list after replacement
    """
    new_list = [0] * len(my_list)
    for i in range(len(new_list)):
        if (my_list[i] == search):
            new_list[i] = replace
        else:
            new_list[i] = my_list[i]

    return new_list
