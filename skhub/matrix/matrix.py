#!/usr/bin/env python3
"""
This module implements the Matrix class and a factory function.

The Matrix class is a dict-like structure that is indexed by the tuple (x, y),
representing the coordinate of the element in the matrix.

It features a `print` method that aims to provide a graphic representation of
the matrix separating its elements by a space. The optional parameter `pretty`
can be used to control cell width in order to print matrices in a way that is
easier to visualize by humans.
"""

from abc import ABC, abstractmethod


class Formula(ABC):
    """
    An abstract base class that represents a matrix formula.
    """

    @abstractmethod
    def __init__(self, m, n, number_generator):
        self.m, self.n = m, n

    @abstractmethod
    def get(self, x, y):
        if x >= self.m or y >= self.n:
            raise IndexError("matrix index out of range")


class Matrix:
    """
    A class that represents a matrix.
    """

    def __init__(self, m, n):
        """
        Initialize the Matrix class.

        Args:
            m (int): The quantity of rows.
            n (int): The quantity of columns.
   
        """
        self.m, self.n = m, n
        self.data = {}
        for i in range(m):
            for j in range(n):
                self.data[(i, j)] = None

    def __repr__(self):
        return f"Matrix({self.m}, {self.n})"

    def __str__(self):
        return str(self.data)

    def __getitem__(self, key):
        return self.data[key]

    def __setitem__(self, key, value):
        self.data[key] = value

    def print(self, pretty=False):
        """
        Print the matrix on the console.

        An optional parameter `pretty` constrols if spaces are padded to
        justify cell contents to the right or if single spaces between cells
        should be used (default).

        Args:
            pretty (bool) [optional]: A flag to control if pretty printing.
            Defaults to False.

        Sample usage:
            >>> matrix_factory(20, 20, prime, N_of_x_plus_N_of_y).print()
            4 5 7 9 13 15 19 21 25 31 33 39 43 45 49 55 61 63 69 73
            5 6 8 10 14 16 20 22 26 32 34 40 44 46 50 56 62 64 70 74
            7 8 10 12 16 18 22 24 28 34 36 42 46 48 52 58 64 66 72 76
            9 10 12 14 18 20 24 26 30 36 38 44 48 50 54 60 66 68 74 78
            13 14 16 18 22 24 28 30 34 40 42 48 52 54 58 64 70 72 78 82
            15 16 18 20 24 26 30 32 36 42 44 50 54 56 60 66 72 74 80 84
            19 20 22 24 28 30 34 36 40 46 48 54 58 60 64 70 76 78 84 88
            21 22 24 26 30 32 36 38 42 48 50 56 60 62 66 72 78 80 86 90
            25 26 28 30 34 36 40 42 46 52 54 60 64 66 70 76 82 84 90 94
            31 32 34 36 40 42 46 48 52 58 60 66 70 72 76 82 88 90 96 100
            33 34 36 38 42 44 48 50 54 60 62 68 72 74 78 84 90 92 98 102
            39 40 42 44 48 50 54 56 60 66 68 74 78 80 84 90 96 98 104 108
            43 44 46 48 52 54 58 60 64 70 72 78 82 84 88 94 100 102 108 112
            45 46 48 50 54 56 60 62 66 72 74 80 84 86 90 96 102 104 110 114
            49 50 52 54 58 60 64 66 70 76 78 84 88 90 94 100 106 108 114 118
            55 56 58 60 64 66 70 72 76 82 84 90 94 96 100 106 112 114 120 124
            61 62 64 66 70 72 76 78 82 88 90 96 100 102 106 112 118 120 126 130
            63 64 66 68 72 74 78 80 84 90 92 98 102 104 108 114 120 122 128 132
            69 70 72 74 78 80 84 86 90 96 98 104 108 110 114 120 126 128 134 138
            73 74 76 78 82 84 88 90 94 100 102 108 112 114 118 124 130 132 138 142

            >>> matrix_factory(20, 20, prime, N_of_x_plus_N_of_y).print(pretty=True)
              4   5   7   9  13  15  19  21  25  31  33  39  43  45  49  55  61  63  69  73
              5   6   8  10  14  16  20  22  26  32  34  40  44  46  50  56  62  64  70  74
              7   8  10  12  16  18  22  24  28  34  36  42  46  48  52  58  64  66  72  76
              9  10  12  14  18  20  24  26  30  36  38  44  48  50  54  60  66  68  74  78
             13  14  16  18  22  24  28  30  34  40  42  48  52  54  58  64  70  72  78  82
             15  16  18  20  24  26  30  32  36  42  44  50  54  56  60  66  72  74  80  84
             19  20  22  24  28  30  34  36  40  46  48  54  58  60  64  70  76  78  84  88
             21  22  24  26  30  32  36  38  42  48  50  56  60  62  66  72  78  80  86  90
             25  26  28  30  34  36  40  42  46  52  54  60  64  66  70  76  82  84  90  94
             31  32  34  36  40  42  46  48  52  58  60  66  70  72  76  82  88  90  96 100
             33  34  36  38  42  44  48  50  54  60  62  68  72  74  78  84  90  92  98 102
             39  40  42  44  48  50  54  56  60  66  68  74  78  80  84  90  96  98 104 108
             43  44  46  48  52  54  58  60  64  70  72  78  82  84  88  94 100 102 108 112
             45  46  48  50  54  56  60  62  66  72  74  80  84  86  90  96 102 104 110 114
             49  50  52  54  58  60  64  66  70  76  78  84  88  90  94 100 106 108 114 118
             55  56  58  60  64  66  70  72  76  82  84  90  94  96 100 106 112 114 120 124
             61  62  64  66  70  72  76  78  82  88  90  96 100 102 106 112 118 120 126 130
             63  64  66  68  72  74  78  80  84  90  92  98 102 104 108 114 120 122 128 132
             69  70  72  74  78  80  84  86  90  96  98 104 108 110 114 120 126 128 134 138
             73  74  76  78  82  84  88  90  94 100 102 108 112 114 118 124 130 132 138 142
        """

        # Calculate cell width when pretty-printing
        cell_width = 0
        if pretty:
            max_number = max(self.data.values())
            cell_width = len(str(max_number))

        # Print matrix
        for x in range(self.m):
            row = []
            for y in range(self.n):
                row.append(self.data[(x, y)])
            print(' '.join([str(n).rjust(cell_width) for n in row]))


def matrix_factory(m, n, number_generator, formula):
    """
    A factory for generating matrices.

    The factory takes parameters controlling the size of the matrix to be
    generated, as well as the iterator to generate the number sequence and the
    formula to use to compute each element of the matrix.

    The only assumption that this factory does about the formula class is that
    it is initialized passing the parameters `m`, `n` and `number_generator`,
    and that it contains a method with the signature `get(x, y)` that returns
    the value to be stored in the matrix for element (x, y).

    Args:
        m (int): The quantity of rows.
        n (int): The quantity of columns.
        number_generator (iterator): The number generator function.
        formula (class): The formula class.

    Returns:
        Matrix: The Matrix instance built with provided arguments.

    Sample usage:
        >>> matrix_factory(20, 30, prime, N_of_x_plus_N_of_y)
        Matrix(20, 30)
    """

    f = formula(m, n, number_generator)
    matrix = Matrix(m, n)

    for i in range(m):
        for j in range(n):
            matrix[(i, j)] = f.get(i, j)

    return matrix
