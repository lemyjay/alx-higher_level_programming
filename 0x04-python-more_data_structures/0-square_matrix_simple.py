#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    temp = matrix.copy()
    new_matrix = []
    for i in temp:
        row = list(map(lambda x: x * x, i))
        new_matrix.append(row)
    return new_matrix
