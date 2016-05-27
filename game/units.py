from gfx import HeroGfx, EnemiGfx, BrickGfx


class Unit(object):
    v = 40
    direction = None

    def __init__(self):
        raise NotImplementedError("Unit is abstract type")

    def set_position(self, x, y):
        self.gfx.set_position(x, y)

    def move_up(self, dt):
        self.move(dt, 'up')

    def move_down(self, dt):
        self.move(dt, 'down')

    def move_left(self, dt):
        self.move(dt, 'left')

    def move_right(self, dt):
        self.move(dt, 'right')

    def move(self, dt, direction):
        self.direction = direction

    def update(self, dt):
        if not self.direction:
            return
        self.gfx.set_animation(self.direction)
        direction = {
            'up': (0, 1),
            'down': (0, -1),
            'left': (-1, 0),
            'right': (1, 0)
        }[self.direction]
        x = self.gfx.pos[0] + direction[0]*dt*self.v
        y = self.gfx.pos[1] + direction[1]*dt*self.v
        self.gfx.set_position(x, y)
        self.direction = None


class Hero(Unit):

    def __init__(self):
        self.gfx = HeroGfx()


class Enemi(Unit):

    def __init__(self):
        self.gfx = EnemiGfx()


class Brick(Unit):

    def __init__(self):
        self.gfx = BrickGfx()
