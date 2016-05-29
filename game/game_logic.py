from kivy.uix.widget import Widget

from core.statemanager import State
import game_rules 
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
        self.root_widget.parent.resize(w, h)
        self.physics = Physics(w, h)

        units = [self.add_hero(lvl.units_symbols['h'][0], 100, 100)]
        for (collision_type, unit_factory, x, y) in lvl.iter():
            unit = self.add_unit(unit_factory, collision_type, x, y)
            units.append(unit)

        self.units = units

        # build call backs for collision
        self.physics.space.add_collision_handler(
            lvl.units_symbols['h'][0],
            lvl.units_symbols['e'][0],
            post_solve=game_rules.collision_hero_enemy
        )

    def add_unit(self, unit_factory, collision_type, x, y):
        u = unit_factory(collision_type)
        u.set_position(x, y)
        self.physics.add_body(u)
        self.root_widget.add_widget(u.gfx)
        return u

    def add_hero(self, collision_type, x, y):
        hero = self.add_unit(Hero, collision_type, x, y)

        movements = {
            'up': lambda dt: hero.move_up(dt),
            'down': lambda dt: hero.move_down(dt),
            'left': lambda dt: hero.move_left(dt),
            'right': lambda dt: hero.move_right(dt),
        }

        for d, a in movements.iteritems():
            self.event_manager.register_action(d, a)

        return hero
