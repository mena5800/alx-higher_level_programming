#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    '''
    return square matrix without change the original one

    Args:
        matrix (2-d list): a matrix of numbers

    Returns:
        a new matrix has square values of original one
    '''
    if (matrix is None):
        return None
    return list(map(lambda row: list(map(lambda x: x ** 2, row)), matrix))
