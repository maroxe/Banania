import random


class UnitAi(object):

    def update(self, dt, unit):
        pass


class EnemyFollowingTargetAi(object):

    power_follow = 60/50.

    def __init__(self, target):
        self.target = target

    def update(self, dt, unit):
        if random.random() < dt*self.power_follow:
            u = (self.target.get_position() - unit.get_position())
            unit.move(dt, u)
