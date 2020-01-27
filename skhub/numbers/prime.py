#!/usr/bin/env python3
"""
This module implements a generator for prime numbers.
"""

from itertools import count


def prime_generator():
    """
    An iterator that generates prime numbers by using the Sieve of Eratosthenes
    algorithm.

    The sieve is created as the generator goes through its iterations, adding
    to the sieve the next composite numbers for every prime it identifies.
    """

    yield 2
    sieve = {}

    for i in count(3, 2):
        composite = sieve.pop(i, None)

        if not composite:
            yield i
            sieve[i*i] = 2*i

        else:
            # Add next composite to sieve
            x = i + composite
            while x in sieve:
                x += composite
            sieve[x] = composite
