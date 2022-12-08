#!/usr/bin/python3
def square_matrix_simple(matrix=[]):

    new_matrix = []

    for i in matrix:
        new_copy = list(map(lambda x: x * x, i))
        new_matrix.append(new_copy)
    return new_matrix
