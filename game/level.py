from units import Hero, Enemi, Brick


class Level:
    units_symbols = {
        'h': Hero,
        'e': Enemi,
        'b': Brick
    }

    def __init__(self, level_file):
        with open(level_file) as f:
            self.header = map(int, f.readline().split())
            self.units = map(self.read_line, f.readlines())

    def get_header(self):
        return self.header

    def read_line(self, line):
        u, x, y = line.split()
        return (self.units_symbols[u], int(x), int(y))

    def iter(self):
        return self.units
