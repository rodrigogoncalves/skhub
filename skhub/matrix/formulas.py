from itertools import islice

class N_of_x_plus_N_of_y:
    def __init__(self, m, n, number_generator):
        self.numbers = list(islice(number_generator(), 0, max(m, n)))
    def get(self, x, y):
        return self.numbers[x] + self.numbers[y]

class N_of_x_times_N_of_y:
    def __init__(self, m, n, number_generator):
        self.numbers = list(islice(number_generator(), 0, max(m, n)))
    def get(self, x, y):
        return self.numbers[x] * self.numbers[y]

class N_of_x_plus_y_plus_1:
    def __init__(self, m, n, number_generator):
        self.numbers = list(islice(number_generator(), 0, m+n+1))
    def get(self, x, y):
        return self.numbers[x+y+1]
