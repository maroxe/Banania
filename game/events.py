from kivy.uix.widget import Widget
from kivy.vector import Vector


class EventManager(Widget):

    actions = {}
    events = {'swipe': None}

    def register_action(self, key, action):
        self.actions[key] = action

    def on_touch_up(self, touch):
        u = Vector(touch.pos) - Vector(touch.opos)
        self.on_swipe(u)

    def on_swipe(self, direction):
        self.events['swipe'] = direction

    def update(self, dt):
        for key, action in self.actions.items():
            if self.events[key]:
                print 'self.events[key]', self.events[key]
                action(dt, self.events[key])
        self.events = {'swipe': None}
