#!/usr/bin/python3
def weight_average(my_list=[]):
    """
    returns the weighted average of all integers tuple (<score>, <weight>)

    Args:
        my_list (list, optional): list. Defaults to [].

    Returns:
        number: weighted average of all integers tuple
    """
    if (my_list is None or len(my_list) == 0):
        return 0

    number = 0
    sum = 0
    for (x, y) in my_list:
        number += x * y
        sum += y

    return number / sum
