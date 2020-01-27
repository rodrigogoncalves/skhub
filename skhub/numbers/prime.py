from itertools import count

def prime_generator():
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
