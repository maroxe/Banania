from gfx import HeroGfx, EnemiGfx, BrickGfx


class Unit(object):

    def __init__(self):
        raise NotImplementedError("Unit is abstract type")

    def set_position(self, x, y):
        self.gfx.set_position(x, y)

    def move_up(self, dt):
        v = 100
        self.gfx.set_position(self.gfx.pos[0], self.gfx.pos[1]+dt*v)
        self.gfx.img.source = self.gfx.walk


class Hero(Unit):

    def __init__(self):
        self.gfx = HeroGfx()


class Enemi(Unit):

    def __init__(self):
        self.gfx = EnemiGfx()


class Brick(Unit):

    def __init__(self):
        self.gfx = BrickGfx()
