import random


class UnitAi(object):

    def update(self, dt, unit):
        pass


class EnemyFollowingTargetAi(object):

    def __init__(self, target):
        self.target = target

    def update(self, dt, unit):
        u = self.target.get_position() - unit.get_position()
        if random.random() > 55*dt:
            unit.move(dt, u)
