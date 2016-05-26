from kivy.uix.widget import Widget


class EventManager(Widget):

    actions = {}
    events = dict(zip(*(['left', 'right', 'up', 'down'], [False]*4)))
    clean_events = dict(zip(*(['left', 'right', 'up', 'down'], [False]*4)))

    def register_action(self, key, action):
        self.actions[key] = action

    def on_touch_down(self):
        self.events = dict(self.clean_events)
        self.events['down'] = True

    def on_touch_up(self):
        self.events = dict(self.clean_events)
        self.events['up'] = True

    def on_touch_left(self):
        self.events = dict(self.clean_events)
        self.events['left'] = True

    def on_touch_right(self):
        self.events = dict(self.clean_events)
        self.events['right'] = True

    def update(self, dt):
        for event, action in self.actions.items():
            if self.events[event]:
                action(dt)
