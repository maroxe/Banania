import random


class UnitAi(object):

    def update(self, dt, unit):
        pass


class EnemyFollowingTargetAi(object):

    power_follow = 60.

    def __init__(self, target):
        self.target = target

    def update(self, dt, unit):
        u = (self.target.get_position() - unit.get_position())
        u *= dt * self.power_follow

        if random.random() > 50*dt:
            unit.move(dt, u)
