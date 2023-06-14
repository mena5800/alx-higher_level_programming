#!/usr/bin/python3
def common_elements(set_1, set_2):
    """
    returns a set of common elements in two sets.

    Args:
        set_1 (set): first set
        set_2 (set): second set

    Return:
        returns a set of common elements in two sets
    """
    items = set()
    for item in set_1:
        if (item in set_2):
            items.add(item)

    return items

