from units import *


class Level:
    units_symbols = {
        'h': (10, Hero),
        'e': (20, Enemy),
        'b': (0, Brick)
    }

    def __init__(self, level_file):
        with open(level_file) as f:
            self.header = map(int, f.readline().split())
            self.units = map(self.read_line, f.readlines())

    def get_header(self):
        return self.header

    def read_line(self, line):
        u, x, y = line.split()
        collision_type, symbol = self.units_symbols[u]
        return (collision_type, symbol, int(x), int(y))

    def iter(self):
        return self.units
