#!/usr/bin/python3
"""
    100-matrix_mul Module
"""


def matrix_mul(m_a, m_b):
    """
     function that multiplies 2 matrices

     Args:
            m_a: first matrix(2D List)
            m_b: second matrix(2D List)

        Returns:
            the product of two matrices
    """

    if type(m_a) is not list:
        raise TypeError("m_a must be a list")
    if type(m_b) is not list:
        raise TypeError("m_b must be a list")
    if not m_a:
        raise ValueError("m_a can't be empty")
    if not m_b:
        raise ValueError("m_b can't be empty")

    r_len = 0
    for rows in m_a:
        if type(rows) is not list:
            raise TypeError("m_a must be a list of lists")
        if not rows:
            raise TypeError("m_a can't be empty")
        for elements in rows:
            if type(element) is not int and type(element) is not float:
                raise TypeError("m_a should contain only integers or floats")
        if len(rows) != r_len and r_len != 0:
            raise TypeError("each row of m_a must be of the\
                    same size")
        r_len = len(rows)

    r_len = 0
    for rows in m_b:
        if type(rows) is not list:
            raise TypeError("m_b must be a list of lists")
        if not rows:
            raise TypeError("m_b can't be empty")
        for elements in rows:
            if type(element) is not int and type(element) is not float:
                raise TypeError("m_b should contain only integers or floats")
        if len(rows) != r_len and r_len != 0:
            raise TypeError("each row of m_b must be of the same size
")
            r_len = len(rows)

    # check the order no of clmn in m_a == no or wows in m_b
    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    new_matrix = list()
    for row_a in range(len(m_a)):
        flag = 0
        inner_list = list()
        for row_b in range(len(m_b)):
            for col in range(len(m_b[row_b])):
                if flag == 0:
                    inner_list.append(m_a[row_a][row_b] * m_b[row_b][col])
                else:
                    inner_list[col] += (m_a[row_a][row_b] * m_b[row_b][col])
            flag = 1
        new_matrix.append(inner_list)
        return new_matrix
