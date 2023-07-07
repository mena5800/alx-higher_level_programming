#!/usr/bin/python3
''' module has one function add_integer
'''
def add_integer(a, b=98):
    '''
    this function takes two numbers as input and return their sum.

    parameters:
    a (int or float): the first number to add.
    b (int or float): the second number to add.

    Returns:
    int: the sum of the two numbers.
    '''
    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")
    if type(b) not in [int, float]:
        raise TypeError("b must be an integer")

    if type(a) == float:
        a = int(a)
    if type(b) == float:
        b = int(b)

    return a + b
