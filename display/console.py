#!/usr/bin/env python3
"""
This module implements a function to print square matrices on the console.
"""


def print_square_matrix(m, pretty=False):
    """
    Print a square matrix on the console.

    The parameter `m` is a 2-dimensional list that needs to have the same
    number of elements of rows and in each column.

    An optional parameter `pretty` constrols if spaces are padded to justify
    cell contents to the right or if single spaces between cells should be
    used (default).

    Args:
        m (list): A list of rows, which are lists of columns.
        pretty (bool) [optional]: A flag to control if pretty printing.
        Defaults to False.

    Raises:
        ValueError: If `m` does not represent a square matrix.

    Sample usage:
        >>> print_square_matrix([[0, 1], [0, 1]])
        0 1
        0 1

        >>> print_square_matrix([[0, 1], [0]])
        Traceback (most recent call last):
        ValueError: matrix is not square
    """

    rows = len(m)
    cols = 0
    for i in range(0, rows):
        cols = len(m[i])
        if rows != cols:
            raise ValueError("matrix is not square")

    cell_width = 0
    if pretty and rows and cols:
        last_prime = m[:1][0][:1][0]
        cell_width = len(str(last_prime))*2

    for x in range(0, rows):
        row = []
        for y in range(0, cols):
            row.append(m[x][y])
        print(' '.join([str(n).rjust(cell_width) for n in row]))


if __name__ == '__main__':
    import doctest
    import sys

    doctest.testmod()

    if len(sys.argv) > 1:
        n = int(sys.argv[1])
        data = []
        for i in range(0, n):
            row = []
            for j in range(0, n):
                row.append(1 if i == j else 0)
            data.append(row)
        print_square_matrix(data)
