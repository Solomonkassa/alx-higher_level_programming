#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = []
    for row in matrix:
        transpose = []
        for elem in row:
            elem = elem * elem
            transpose.append(elem)
        new_matrix.append(transpose)
    return new_matrix
