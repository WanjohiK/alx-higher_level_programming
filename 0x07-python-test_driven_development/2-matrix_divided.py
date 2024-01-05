#!/usr/bin/python3
"""
2-matrix_divided Module
"""


def matrix_divided(matrix, div):
    """
    function that divides elements of a matrix

    Args:
        matrix: 2D lists
        div: divisor type int

    Returns:
        new matrix with divided elements
        in 2 dp
    """
    curr_len = 0
    error_msg = "matrix must be a matrix (list of lists) of integers/floats"
    if type(matrix) is not list:
        raise TypeError(error_msg)

    for rows in matrix:    # matrix is a list
        if type(rows) is not list:
            raise TypeError(error_msg)

        for element in rows:
            if type(element) is not int and type(element) is not float:
                raise TypeError(error_msg)

        if len(rows) != curr_len and curr_len != 0:
            raise TypeError("Each row of the matrix must have the same size")
        curr_len = len(rows)

    if type(div) is not int and type(div) is not float:
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    return [[round(elem / div, 2) for elem in row] for row in matrix]
