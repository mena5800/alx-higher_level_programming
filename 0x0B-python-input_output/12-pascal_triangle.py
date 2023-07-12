#!/usr/bin/python3

"""
this module contain function pascal_triangle
"""


def pascal_triangle(n):
    """
    returns a list of lists of integers representing
    the Pascal's triangle of n:
    """
    if n <= 0:
        return []

    result = []
    for i in range(n):
        new_list = []
        for j in range(i+1):
            if j == 0 or j == i:
                new_list.append(1)
            else:
                new_list.append(result[i-1][j-1]+result[i-1][j])

        result.append(new_list)

    return result
