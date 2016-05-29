import pymunk


class Physics:
    def __init__(self, w, h):
        self.space = pymunk.Space()
        self.space.gravity = (0, 0)

        body = pymunk.Body()
        body.position = (0, 0)
        # limits of the arena
        l1 = pymunk.Segment(body, (0, 0), (0, h), 1)
        l2 = pymunk.Segment(body, (w+0, 0), (w+0, h), 1)
        l3 = pymunk.Segment(body, (0, -0), (w, -0), 1)
        l4 = pymunk.Segment(body, (0, h-0), (w, h-0), 1)
        l1.elasticity = 1
        l2.elasticity = 1
        l3.elasticity = 1
        l4.elasticity = 1
        self.space.add(l1, l2, l3, l4)

    def add_body(self, unit):
        self.space.add(unit.physics.body, unit.physics.poly)

    def update(self, dt):
        self.space.step(dt)


class UnitPhysics:
    def __init__(self, collision_type):
        print(collision_type)
        self.body = pymunk.Body(1, 1)
        self.radius = 32
        self.poly = pymunk.Circle(self.body, self.radius)
        self.poly.elasticity = 0.7
        self.poly.collision_type = collision_type

        #self.poly = pymunk.Poly.create_box(self.body)

    def get_position(self):
        return self.body.position - (self.radius, self.radius)

    def set_position(self, x, y):
        self.body.position = (x+self.radius, y+self.radius)

    def get_rotation(self):
        return self.body.angle
