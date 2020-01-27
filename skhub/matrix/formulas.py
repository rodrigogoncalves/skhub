#!/usr/bin/env python3
"""
This module implements formulas to be used to calculate matrices elements.

The interface of a formula class is defined as having a constructor that is
initialized with the parameters `m`, `n` and `number_generator`, and contains
a method `get(x, y)` that returns the value to be stored in the matrix for
element (x, y).

The formula class receives a number generator since it is responsible for
knowing the numbers it needs to generate in order to perform its calculations.
"""

from itertools import islice

from skhub.matrix import Formula


class N_of_x_plus_N_of_y(Formula):
    """
    A formula class that generates the element (x, y) by N(x) + N(y).
    """

    def __init__(self, m, n, number_generator):
        super().__init__(m, n, number_generator)
        self.numbers = list(islice(number_generator(), 0, max(m, n)))

    def get(self, x, y):
        super().get(x, y)
        return self.numbers[x] + self.numbers[y]


class N_of_x_times_N_of_y(Formula):
    """
    A formula class that generates the element (x, y) by N(x) * N(y).
    """

    def __init__(self, m, n, number_generator):
        super().__init__(m, n, number_generator)
        self.numbers = list(islice(number_generator(), 0, max(m, n)))

    def get(self, x, y):
        super().get(x, y)
        return self.numbers[x] * self.numbers[y]


class N_of_x_plus_y_plus_1(Formula):
    """
    A formula class that generates the element (x, y) by N(x + y + 1).
    """

    def __init__(self, m, n, number_generator):
        super().__init__(m, n, number_generator)
        self.numbers = list(islice(number_generator(), 0, m+n+1))

    def get(self, x, y):
        super().get(x, y)
        return self.numbers[x+y+1]
