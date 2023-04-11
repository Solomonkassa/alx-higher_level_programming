#!/usr/bin/python3
"""returns a list of lists of integers
    representing the Pascal’s triangle of n
"""


def pascal_triangle(n):
    """returns a list of lists of integers
    representing the Pascal’s triangle of n
    """
    if n <= 0:
        return []

    p_list = []
    for line in range(1, n + 1):
        C = 1
        row = []
        for i in range(1, line + 1):
            row.append(C)
            C = C * (line - i) // i
        p_list.append(row)
    return p_list
