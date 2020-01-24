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

        >>> print_square_matrix([[1 if i == j else i*j for i in range(20)] for j in range(20)], pretty=True)
          1   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0
          0   1   2   3   4   5   6   7   8   9  10  11  12  13  14  15  16  17  18  19
          0   2   1   6   8  10  12  14  16  18  20  22  24  26  28  30  32  34  36  38
          0   3   6   1  12  15  18  21  24  27  30  33  36  39  42  45  48  51  54  57
          0   4   8  12   1  20  24  28  32  36  40  44  48  52  56  60  64  68  72  76
          0   5  10  15  20   1  30  35  40  45  50  55  60  65  70  75  80  85  90  95
          0   6  12  18  24  30   1  42  48  54  60  66  72  78  84  90  96 102 108 114
          0   7  14  21  28  35  42   1  56  63  70  77  84  91  98 105 112 119 126 133
          0   8  16  24  32  40  48  56   1  72  80  88  96 104 112 120 128 136 144 152
          0   9  18  27  36  45  54  63  72   1  90  99 108 117 126 135 144 153 162 171
          0  10  20  30  40  50  60  70  80  90   1 110 120 130 140 150 160 170 180 190
          0  11  22  33  44  55  66  77  88  99 110   1 132 143 154 165 176 187 198 209
          0  12  24  36  48  60  72  84  96 108 120 132   1 156 168 180 192 204 216 228
          0  13  26  39  52  65  78  91 104 117 130 143 156   1 182 195 208 221 234 247
          0  14  28  42  56  70  84  98 112 126 140 154 168 182   1 210 224 238 252 266
          0  15  30  45  60  75  90 105 120 135 150 165 180 195 210   1 240 255 270 285
          0  16  32  48  64  80  96 112 128 144 160 176 192 208 224 240   1 272 288 304
          0  17  34  51  68  85 102 119 136 153 170 187 204 221 238 255 272   1 306 323
          0  18  36  54  72  90 108 126 144 162 180 198 216 234 252 270 288 306   1 342
          0  19  38  57  76  95 114 133 152 171 190 209 228 247 266 285 304 323 342   1

        >>> print_square_matrix([[0, 1], [0]])
        Traceback (most recent call last):
        ValueError: matrix is not square
    """

    # Validate if matrix is square
    size = len(m)
    for i in range(size):
        if size != len(m[i]):
            raise ValueError("matrix is not square")

    # Calculate cell width when pretty-printing
    cell_width = 0
    if pretty and size:
        max_number = max(map(max, m))
        cell_width = len(str(max_number))

    # Print matrix
    for x in range(size):
        row = []
        for y in range(size):
            row.append(m[x][y])
        print(' '.join([str(n).rjust(cell_width) for n in row]))


if __name__ == '__main__':
    import doctest
    import sys

    doctest.testmod()

    if len(sys.argv) > 1:
        n = int(sys.argv[1])
        data = []
        for i in range(n):
            row = []
            for j in range(n):
                row.append(1 if i == j else i*j)
            data.append(row)
        print_square_matrix(data)
