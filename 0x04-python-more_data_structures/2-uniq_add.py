#!/usr/bin/python3
def uniq_add(my_list=[]):
    """
    adds all unique integers in a list (only once for each integer).

    Args:
        my_list (list): initial list. Defaults to [].

    Return:
        sum (int): the sum of unique numbers in list.
    """
    my_dict = {}
    sum = 0
    for num in my_list:
        if (my_dict.get(num, None) == None):
            my_dict[num] = 1
            sum += num

    return sum
