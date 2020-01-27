from itertools import count

def fibonacci_generator():
    yield 0
    yield 1
    seq = [0, 1]
    for i in count(2):
        seq.append(seq[i-1] + seq[i-2])
        yield seq[-1:][0]
