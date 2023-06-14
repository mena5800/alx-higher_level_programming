#!/usr/bin/python3

def multiply_list_map(my_list=[], number=0):
    """
    returns a list with all values multiplied by
    a number without using any loops.

    Args:
        my_list (list, optional): list. Defaults to [].
        number (int, optional): number. Defaults to 0.

    Return:
        a new list multiply by number
    """
    def multiply(x):
        """
        multiply by number

        Args:
            x (int): number
        """
        return x * number

    new_list = list(map(multiply, my_list))
    return new_list
