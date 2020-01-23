#!/usr/bin/env python3
"""
This script accepts a single integer parameter and prints a matrix on the
console.

The parameter is the size of the square matrix, and each element of the matrix
with coordinate (a, b) is given by the sum of a-th and b-th prime numbers.
"""

if __name__ == '__main__':
    import sys

    from algorithm import prime
    from display import console

    if len(sys.argv) > 1:
        n = sys.argv[1]
        primes = prime.get_n_primes(n)
        # Force `n` to be an int
        n = len(primes)

        data = []
        for i in range(0, n):
            row = []
            for j in range(0, n):
                row.append(primes[i]+primes[j])
            data.append(row)

        console.print_square_matrix(data)
