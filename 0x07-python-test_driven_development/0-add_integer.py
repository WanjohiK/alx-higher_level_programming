#!/usr/bin/python3
"""
    0-add_integer Module
"""


def add_integer(a, b=98):
    """
    Add two intergers

    Args:
        a: first int
        b: second int

    Returns:
        sum of two integers
    """
    if type(a) is not int and type(a) is not float:
        raise TypeError("a must be an integer")
    elif type(b) is not int and type(b) is not float:
        raise TypeError("b must be an integer")
    else:
        a, b = int(a), int(b)
        return a + b
