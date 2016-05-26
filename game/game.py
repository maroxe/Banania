from kivy.app import App
from kivy.clock import Clock
from kivy.factory import Factory

from core.statemanager import State
from gfx import Window
from units import Hero
from events import EventManager
from level import Level


def print_msg_callback(s):
    def callback(_):
        print(s)
    return callback



class GameApp(App):

    def build(self):
        self.event_manager = EventManager()
        self.event_manager.register_action('down',
                                           print_msg_callback('down key'))
        window = Window()
        window.event_manager = self.event_manager
        self.window = window
        Clock.schedule_interval(self.update, 1.0/60.0)
        h = self.add_hero(20, 20)

        def move_up(dt):
            h.move_up(dt)

        self.event_manager.register_action('up',
                                           move_up)
        self.build_level()
        return window

    def build_level(self):
        level_file = 'lvl/level1.lvl'
        lvl = Level(level_file)
        w, h = lvl.get_header()
        self.window.resize(w, h)

        for (unit_factory, x, y) in lvl.iter():
            unit = unit_factory()
            unit.set_position(x, y)
            self.window.add_widget(unit.gfx)

    def add_hero(self, x, y):
        hero = Hero()
        hero.set_position(x, y)
        self.window.add_widget(hero.gfx)
        return hero

    def update(self, dt):
        self.event_manager.update(dt)
