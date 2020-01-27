
class Matrix:
    def __init__(self, m, n):
        self.m, self.n = m, n
        self.data = {}
        for i in range(m):
            for j in range(n):
                self.data[(i, j)] = None
    def __repr__(self):
        return f"Matrix({self.m}, {self.n})"
    def __str__(self):
        return str(self.data)
    def __getitem__(self, key):
        return self.data[key]
    def __setitem__(self, key, value):
        self.data[key] = value
    def print(self, pretty=False):

        # Calculate cell width when pretty-printing
        cell_width = 0
        if pretty:
            max_number = max(self.data.values())
            cell_width = len(str(max_number))

        # Print matrix
        for x in range(self.m):
            row = []
            for y in range(self.n):
                row.append(self.data[(x, y)])
            print(' '.join([str(n).rjust(cell_width) for n in row]))


def matrix_factory(m, n, number_generator, formula):
    f = formula(m, n, number_generator)
    matrix = Matrix(m, n)
    for i in range(m):
        for j in range(n):
            matrix[(i, j)] = f.get(i, j)
    return matrix
