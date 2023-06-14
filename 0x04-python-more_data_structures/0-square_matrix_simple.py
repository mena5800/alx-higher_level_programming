#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    '''
    return square matrix without change the original one

    Args:
        matrix (2-d list): a matrix of numbers

    Returns:
        a new matrix has square values of original one
    '''
    new_matrix = [[0]*len(matrix[0])] * len(matrix)
    for i in range(len(new_matrix)):
        for j in range(len(new_matrix[0])):
            new_matrix[i][j] = matrix[i][j] ** 2

    return new_matrix
