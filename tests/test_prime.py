from hypothesis import given
from hypothesis.strategies import integers

from algorithm import prime


def is_prime_6(n):
    if n <= 3:
        return bool(n > 1)
    elif n % 2 == 0 or n % 3 == 0:
        return False

    i = 5

    while i*i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6

    return True

@given(n=integers())
def test_is_prime(n):
    assert is_prime_6(n) == prime.is_prime(n)
