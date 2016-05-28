from kivy.uix.widget import Widget

from core.statemanager import State
from physics import Physics
from events import EventManager
from units import Hero
from level import Level


class GameLogic(State):

    def __init__(self):
        self.event_manager = EventManager()


    def build_widget(self):
        self.root_widget = Widget()
        return self.root_widget

    def update(self, dt):
        self.event_manager.update(dt)
        if not self.is_paused:
            self.physics.update(dt)
            for u in self.units:
                u.update(dt)
        return True

    def build_level(self):
        level_file = 'lvl/level1.lvl'
        lvl = Level(level_file)
        w, h = lvl.get_header()
        self.physics = Physics(w, h)
        self.root_widget.parent.resize(w, h)

        units = [self.add_hero(100, 100)]
        for (unit_factory, x, y) in lvl.iter():
            unit = self.add_unit(unit_factory, x, y)
            units.append(unit)
        self.units = units

    def add_unit(self, unit_factory, x, y):
        u = unit_factory()
        u.set_position(x, y)
        self.physics.add_body(u)
        self.root_widget.add_widget(u.gfx)
        return u

    def add_hero(self, x, y):
        hero = self.add_unit(Hero, x, y)

        movements = {
            'up': lambda dt: hero.move_up(dt),
            'down': lambda dt: hero.move_down(dt),
            'left': lambda dt: hero.move_left(dt),
            'right': lambda dt: hero.move_right(dt),
        }

        for d, a in movements.iteritems():
            self.event_manager.register_action(d, a)

        return hero
