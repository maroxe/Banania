from units import *


class Level:
    units_symbols = {
        'h': Hero,
        'e': Enemy,
        'b': Brick,
        'g': Goal
    }

    def __init__(self, level_file):
        self.units = {
            'h': [],   # hero
            'b': [],   # ball
            'eh': [],  # enemy following hero
            'eb': [],  # enemy following ball
            'eg': [],  # enemy following goal
            'g': []
        }

        with open(level_file) as f:
            self.header = map(int, f.readline().split())
            self.lines = map(self.read_line, f.readlines())

        for (sym, x, y) in self.lines:
            self.units[sym].append((x, y))

    def get_header(self):
        return self.header

    def read_line(self, line):
        u, x, y = line.split()
        return (u, int(x), int(y))

    def iter(self):
        return self.lines
