#!/usr/bin/python3
"""
    4-print_square Module
"""


def print_square(size):
    """
    Prints in stdout the square with the character #

    Args:
    size(int): length of square

    Returns: #square
    """

    if type(size) is not int:
        raise TypeError("size must be an integer")
    elif size < 0:
        raise ValueError("size must be >= 0")
    else:
        for length in range(size):
            for width in range(size):
                print("#", end='')
            print()
