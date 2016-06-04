from kivy.uix.widget import Widget
from kivy.vector import Vector


class EventManager(Widget):

    actions = {}
    empty_events = {'swipe': None, 'double tap': None}
    events = {'swipe': None, 'double tap': None}

    def register_action(self, key, action):
        self.actions[key] = action

    def on_touch_up(self, touch):
        u = Vector(touch.pos) - Vector(touch.opos)
        self.on_swipe(u)

    def on_touch_down(self, touch, *args):
        u = Vector(touch.pos)
        if touch.is_double_tap:
            self.on_double_tap(u)

    def on_swipe(self, direction):
        self.events['swipe'] = direction

    def on_double_tap(self, pos):
        self.events['double tap'] = pos

    def update(self, dt):
        for key, action in self.actions.items():
            if self.events[key]:
                action(dt, self.events[key])
        self.events = dict(self.empty_events)
