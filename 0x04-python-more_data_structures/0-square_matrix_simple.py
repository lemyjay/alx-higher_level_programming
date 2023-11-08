#!/bin/usr/python3

def square_matrix_simple(matrix=[]):
    temp = matrix.copy()
    c = []
    for i in temp:
        r = list(map(lambda x: x * x, i))
        c.append(r)
    return c
