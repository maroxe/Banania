from core.math import Vector2d
from gfx import HeroGfx, EnemyGfx, BrickGfx, GoalGfx
from physics import UnitPhysics


class Unit(object):
    """
    Game units are building block of the game: heros, enemies, bricks ...
    A unit has:
    - a graphical component for drawing on the screen and animation.
    - a physical components for physical simulation and handling collision.
    - a AI component.
    """
    physics_factory = None
    gfx_factory = None
    ai = None

    v = 1000
    direction = None

    def __init__(self):
        self.gfx = self.gfx_factory()
        radius = self.gfx.size[0]/2
        mass = self.gfx.mass
        shape = self.gfx.shape
        collision_type = self.gfx.collision_type
        self.physics = self.physics_factory(
            radius,
            shape,
            mass,
            collision_type)
        self.physics.body.unit = self

    def add_ai(self, ai):
        self.ai = ai

    def get_position(self):
        return Vector2d(self.physics.body.position)

    def set_position(self, x, y):
        self.physics.set_position(x, y)
        self.gfx.set_position(x, y)

    def apply_torque(self):
        self.physics.body.apply_impulse((-2, 0), (0, 32))

    def move(self, dt, direction):
        direction = Vector2d(direction)
        self.direction = direction.normalize()

    def apply_force(self, f):
        self.physics.body.apply_impulse(f*500)

    def update(self, dt):
        # update ai
        if self.ai:
            self.ai.update(dt, self)

        # update gfx
        self.gfx.set_position(*self.physics.get_position())
        self.gfx.set_rotation(self.physics.get_rotation())

        # update mvt
        if not self.direction:
            return
        # self.gfx.set_animation(self.direction)
        x = self.direction[0]*dt*self.v
        y = self.direction[1]*dt*self.v
        self.physics.body.apply_impulse((x, y))

        self.direction = None


class Hero(Unit):
    v = 5000
    physics_factory = UnitPhysics
    gfx_factory = HeroGfx

    def move(self, dt, direction):
        direction = Vector2d(direction)
        self.direction = direction.normalize()*50


class Enemy(Unit):

    physics_factory = UnitPhysics
    gfx_factory = EnemyGfx
    hero = None


class Brick(Unit):

    physics_factory = UnitPhysics
    gfx_factory = BrickGfx


class Goal(Unit):

    physics_factory = UnitPhysics
    gfx_factory = GoalGfx
