from kivy.core.window import Window as KivyWindow
from kivy.uix.widget import Widget
from kivy.vector import Vector

USE_KEYBOARD = False


class EventManager(Widget):

    actions = {}
    empty_events = {'swipe': None, 'double tap': None, 'key down': None}
    events = {'swipe': None, 'double tap': None, 'key down': None}

    def __init__(self, **kwargs):
        super(Widget, self).__init__(**kwargs)
        if USE_KEYBOARD:
            self._keyboard = KivyWindow.request_keyboard(self.on_keyboard_closed, self)
            self._keyboard.bind(on_key_down=self.on_keyboard_down)
            self._keyboard.bind(on_key_up=self.on_keyboard_up)

    def on_keyboard_closed(self):
        self._keyboard.unbind(on_key_down=self._on_keyboard_down)
        self._keyboard = None

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

    def on_keyboard_down(self, keyboard, keycode, text, modifiers):
        self.events['key down'] = keycode[1]
        return True

    def on_keyboard_up(self, keyboard, keycode):
        self.events['key down'] = keycode[1]
        return True

    def update(self, dt):
        for key, action in self.actions.items():
            if self.events[key]:
                action(dt, self.events[key])
        self.events = dict(self.empty_events)
