#!/usr/bin/env python3
"""
This module implements functions to deal with prime number checking and
generation.

The algorithms implemented are the simplest available for each given task. The
rationale is to deliver a working module as soon as possible, and to avoid
premature optimization, since the domain of the problem initially proposed
is very small. If the necessity of expanding the domain of the problem by
powers of ten arises, the functions can be implemented using more sophisticated
algorithms that are faster and more memory efficient, such as the Sieve of
Eratosthenes and its improved variants.
"""

from itertools import count
from math import sqrt


def is_prime(n):
    """
    Return True if `n` is a prime number and False otherwise.

    This function implements a slightly improved version of the naive algorithm
    for prime number checking, considering the upper bound of the range of
    numbers to check the square root of `n`, instead of `n`.

    Args:
        n (int): The number to be checked.

    Returns:
        bool: True if `n` is a prime number and False otherwise.

    Raises:
        ValueError: If `n` is not a valid integer, or cannot be truncated to an
        Integral.

    Sample usage:
        >>> is_prime(2)
        True

        >>> is_prime(3)
        True

        >>> is_prime(10)
        False

        >>> is_prime(11)
        True

        >>> is_prime(3.0)
        True

        >>> is_prime('3.0')
        Traceback (most recent call last):
        ValueError: invalid literal for int() with base 10: '3.0'

        >>> is_prime('a')
        Traceback (most recent call last):
        ValueError: invalid literal for int() with base 10: 'a'
    """

    n = int(n)

    if n < 2:
        return False

    for i in range(2, int(sqrt(n)+1)):
        if n % i == 0:
            return False

    return True


def get_n_primes(n):
    """
    Return an ordered list of `n` prime numbers.

    Args:
        n (int): The quantity of prime numbers to get.

    Returns:
        list: An ordered list of `n` prime numbers.

    Raises:
        ValueError: If `n` is not a valid integer, or cannot be truncated to an
        Integral.

    Sample usage:
        >>> get_n_primes(3)
        [2, 3, 5]

        >>> get_n_primes(10)
        [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]

        >>> get_n_primes(3.0)
        [2, 3, 5]

        >>> get_n_primes('3.0')
        Traceback (most recent call last):
        ValueError: invalid literal for int() with base 10: '3.0'

        >>> get_n_primes('a')
        Traceback (most recent call last):
        ValueError: invalid literal for int() with base 10: 'a'
    """

    primes = []
    n = int(n)
    idx = 2

    while len(primes) < n:
        for i in count(idx):
            if is_prime(i):
                primes.append(i)
                idx = i+1
                break

    return primes


if __name__ == "__main__":
    import doctest
    import sys

    doctest.testmod()

    if len(sys.argv) > 1:
        print(get_n_primes(sys.argv[1]))
