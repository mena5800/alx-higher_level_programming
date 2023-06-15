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
    new_matrix = [[0 for _ in range(3)] for _ in range(3)]
    for i in range(len(new_matrix)):
        for j in range(len(new_matrix[0])):
            new_matrix[i][j] = matrix[i][j] ** 2

    return new_matrix
