import random

from gfx import HeroGfx, EnemiGfx, BrickGfx
from physics import UnitPhysics


class Unit(object):
    v = 10000
    direction = None

    def __init__(self):
        raise NotImplementedError("Unit is abstract type")

    def set_position(self, x, y):
        self.physics.set_position(x, y)
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
        self.gfx.set_position(*self.physics.get_position())
        self.gfx.set_rotation(self.physics.get_rotation())
        if not self.direction:
            return
        self.gfx.set_animation(self.direction)
        direction = {
            'up': (0, 1),
            'down': (0, -1),
            'left': (-1, 0),
            'right': (1, 0)
        }[self.direction]
        x = direction[0]*dt*self.v
        y = direction[1]*dt*self.v
        self.physics.body.apply_impulse((x, y))
        self.direction = None


class Hero(Unit):

    def __init__(self):
        self.gfx = HeroGfx()
        self.physics = UnitPhysics()


class Enemi(Unit):

    def __init__(self):
        self.gfx = EnemiGfx()
        self.physics = UnitPhysics()

    def update(self, dt):
        # move randomly
        if random.random() > 50*dt:
            random.choice([
                self.move_up,
                self.move_down,
                self.move_left,
                self.move_right
            ])(dt)
        super(self.__class__, self).update(dt)


class Brick(Unit):

    def __init__(self):
        self.gfx = BrickGfx()
        self.physics = UnitPhysics()
