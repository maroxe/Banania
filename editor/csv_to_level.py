import csv_grid

input_csv = '../lvl/level1.csv'
output_lvl = '../lvl/level1.lvl'

HIGHT = WIDTH = 32*8
N = 8
SPRITE_SIZE = HIGHT / N

# read
with open(input_csv) as f:
    grid = csv_grid.Grid(f.read())
    lines = '\n'.join(map(lambda u: '%s %d %d' % (u[2], u[1]*SPRITE_SIZE, u[0]*SPRITE_SIZE), grid.symbols))

# write
with open(output_lvl, 'w') as f:
    s = '%d %d\n' % (HIGHT, WIDTH)+ lines
    f.write(s)
