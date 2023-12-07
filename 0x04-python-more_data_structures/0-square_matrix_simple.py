#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    x = []
    for i in matrix:
        x.append(list(map(lambda i: i**2, i)))
    return (x)
