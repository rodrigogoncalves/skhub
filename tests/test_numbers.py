#!/usr/bin/env python3
"""
This module implements tests for skhub.numbers module.
"""

from itertools import islice

import pytest

from skhub.numbers import fibonacci, prime


def test_fibonacci():
    """
    Test fibonacci number generator.
    """

    fibos = list(islice(fibonacci(), 0, 20))
    assert fibos[0] == 0
    assert fibos[1] == 1
    assert fibos[9] == 34
    assert fibos[19] == 4181
    with pytest.raises(IndexError):
        fibos[20]

    fibos = list(islice(fibonacci(), 0, 1001))
    assert fibos[1000] == 43466557686937456435688527675040625802564660517371780402481729089536555417949051890403879840079255169295922593080322634775209689623239873322471161642996440906533187938298969649928516003704476137795166849228875

def test_prime():
    """
    Test prime number generator.
    """

    primes = list(islice(prime(), 0, 20))
    assert primes[0] == 2
    assert primes[1] == 3
    assert primes[9] == 29
    assert primes[19] == 71
    with pytest.raises(IndexError):
        primes[20]

    primes = list(islice(prime(), 0, 1001))
    assert primes[1000] == 7927

    primes = list(islice(prime(), 0, 10001))
    assert primes[10000] == 104743
