from kivy.uix.widget import Widget
from kivy.vector import Vector


class EventManager(Widget):

    actions = {}
    events = dict(zip(*(['left', 'right', 'up', 'down'], [False]*4)))
    clean_events = dict(zip(*(['left', 'right', 'up', 'down'], [False]*4)))

    def register_action(self, key, action):
        self.actions[key] = action

    def on_touch_up(self, touch):
        directions = [['left', 'right'], ['down', 'up']]
        u = Vector(touch.pos) - Vector(touch.opos)
        d = abs(u[0]) < abs(u[1])
        s = u[d] > 0
        self.on_swipe(directions[d][s])

    def on_swipe(self, direction):
        self.events = dict(self.clean_events)
        self.events[direction] = True

    def update(self, dt):
        for event, action in self.actions.items():
            if self.events[event]:
                action(dt)
