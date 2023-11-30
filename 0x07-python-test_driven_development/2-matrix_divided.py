#!/usr/bin/python3
"""
Division of all elements of a matrix
"""


def matrix_divided(matrix, div):
    """
    A function that divides all elements of a matrix

    Args:
        matrix (list): the matrix, a list of lists of integers or floats
        div (int or float): the number by which each element in the matrix
                            would be divided by.

    Returns:
        A new matrix.

    Raises:
        TypeError: if the matrix is not a list of lists or integers or floats
                   if each row of the matrix is not of the same size
                   if div is not a number (integer or float)
        ZeroDivisionError: if div equals 0

    All elements of the matrix should be divided by div and rounded to 2
    decimal places.
    """
    err_matrix = "matrix must be a matrix (list of lists) of integers/floats"
    err_div = "div must be a number"
    err_row = "Each row of the matrix must have the same size"
    err_0 = "division by zero"

    if not isinstance(matrix, list) or len(matrix) == 0 or len(matrix[0]) == 0:
        raise TypeError(err_matrix)
    if not isinstance(div, (int, float)):
        raise TypeError(err_div)
    if div == 0:
        raise ZeroDivisionError(err_0)

    row_len = len(matrix[0])
    new_matrix = []
    for i in matrix:
        if not isinstance(i, list):
            raise TypeError(err_matrix)
        if len(i) != row_len:
            raise TypeError(err_row)

        row = []
        for k in i:
            if not isinstance(k, (int, float)):
                raise TypeError(err_matrix)
            row.append(round(k / div, 2))

        new_matrix.append(row)

    return new_matrix
