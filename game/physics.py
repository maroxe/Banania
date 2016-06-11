import cymunk.cymunk as pm


class Physics:
    """
    Physics Engine. Creates the physical space and updates it
    """

    def __init__(self, w, h):
        self.space = pm.Space()
        self.space.gravity = (0, 0)

        body = pm.Body()
        body.position = (0, 0)
        # limits of the arena
        l1 = pm.Segment(body, (0, 0), (0, h), 10)
        l2 = pm.Segment(body, (w+0, 0), (w+0, h), 10)
        l3 = pm.Segment(body, (0, -0), (w, -0), 10)
        l4 = pm.Segment(body, (0, h-0), (w, h-0), 10)
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
    """
    Spherical physical body
    """

    def __init__(self, radius, shape, mass, collision_type=0):
        self.body = pm.Body(mass, 1)
        self.radius = radius

        if shape == 'circle':
            self.poly = pm.Circle(self.body, self.radius)
        elif shape == 'box':
            self.poly = pm.Poly.create_box(self.body, [self.radius]*2)

        self.poly.elasticity = 0.7
        self.poly.friction = 0.5
        self.poly.collision_type = collision_type

    def get_position(self):
        return self.body.position - (self.radius, self.radius)

    def set_position(self, x, y):
        self.body.position = (x+self.radius, y+self.radius)

    def get_rotation(self):
        return self.body.angle
