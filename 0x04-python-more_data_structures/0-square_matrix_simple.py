#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    copy = [list(map(lambda x: x**2, column)) for column in matrix]
    return copy
