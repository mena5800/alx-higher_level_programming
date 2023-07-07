#!/usr/bin/python3


"""this module has function matrix_divided
"""


def matrix_divided(matrix, div):
    '''
    function that divides all elements of a matrix.

    Arguments:
                matrix: 2-d array
                div: int

        Return:
                matrix // div
    '''
    if type(matrix) is not list:
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats")

    rows = len(matrix[0])
    for i in range(len(matrix)):
        if len(matrix[i]) != rows:
            raise TypeError("Each row of the matrix must have the same size")
        for j in range(len(matrix[0])):
            if type(matrix[i][j]) not in [float, int]:
                raise TypeError(
                    "matrix must be a matrix (list of lists) of integers/floats"
                    )

    if type(div) not in [int, float]:
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    new_matrix = list(map(lambda row: list(
        map(lambda x: round(x/div, 2), row)), matrix))

    return new_matrix
