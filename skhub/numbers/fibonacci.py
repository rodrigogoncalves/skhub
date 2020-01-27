#!/usr/bin/env python3
"""
This module implements a generator for fibonacci numbers.

The iterator starts with 0.
"""

from itertools import count


def fibonacci_generator():
    """
    An iterator that generates fibonacci numbers by using a cache table with
    previous fibonacci numbers.

    The iterator starts with 0.
    """

    yield 0
    yield 1
    seq = [0, 1]

    for i in count(2):
        seq.append(seq[i-1] + seq[i-2])
        yield seq[-1:][0]
