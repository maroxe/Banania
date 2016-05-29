import csv_grid

input_csv = '../lvl/level1.csv'
output_lvl = '../lvl/level1.lvl'

SPRITE_SIZE = 64
N = 10
HIGHT = WIDTH = N * SPRITE_SIZE

# read
with open(input_csv) as f:
    grid = csv_grid.Grid(f.read())
    lines = '\n'.join(map(lambda u: '%s %d %d' % (u[2], u[0]*SPRITE_SIZE, u[1]*SPRITE_SIZE), grid.symbols))

# write
with open(output_lvl, 'w') as f:
    s = '%d %d\n' % (HIGHT, WIDTH)+ lines
    f.write(s)
