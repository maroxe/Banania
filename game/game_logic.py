
import game_rules
from core.statemanager import State
from ui.game_interface import GameInterface
from physics import Physics
from ai import EnemyFollowingTargetAi
from events import EventManager
from units import Hero, Enemy, Brick, Goal
from level import Level


class GameLogic(State):

    time = 0

    def __init__(self):
        self.event_manager = EventManager()

    def build_widget(self):
        self.game_interface = GameInterface()
        return self.game_interface

    def update(self, dt):
        self.time += dt
        self.game_interface.score = self.game_state.score
        self.game_interface.time = self.time
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
        self.game_interface.parent.resize(w, h)
        self.game_interface.size = (w, h)
        self.physics = Physics(w, h)
        hero = self.add_hero(100, 500)
        ball = self.add_ball(200, 100)
        goal = self.add_goal(500, 100)
        old = self.add_enemy_following_target(0, 400, hero)
        units = [hero, ball, old, goal]
        for i in range(5, 5*self.game_state.score):
            units.append(self.add_enemy_following_target(i*30, 400, goal))

        for i in range(5, 5*self.game_state.score):
            new = self.add_enemy_following_target(i*30, 500, hero)
            units.append(new)
            old = new

        # for (unit_factory, x, y) in lvl.iter():
        #     unit = self.add_unit(unit_factory, x, y)
        #     units.append(unit)
        self.units = units

        self.physics.space.add_collision_handler(
            3,  # goal
            4,  # ball
            post_solve=game_rules.collision_ball_border,
            game_logic=self
        )

        def on_double_tap(dt, pos):
            self.add_explosion(hero.get_position())

        self.event_manager.register_action('double tap', on_double_tap)

    def game_ended(self, player_won):
        if player_won:
            self.game_state.score += 1
        else:
            self.game_state.score -= 1
        self.game_state.player_won = player_won
        self.stop()
        self.on_quit()

    def add_unit(self, unit_factory, x, y):
        u = unit_factory()
        u.set_position(x, y)
        self.physics.add_body(u)
        self.game_interface.add_widget(u.gfx)
        return u

    def add_hero(self, x, y):
        hero = self.add_unit(Hero, x, y)
        self.event_manager.register_action('swipe', hero.move)
        return hero

    def add_ball(self, x, y):
        return self.add_unit(Brick, x, y)

    def add_goal(self, x, y):
        return self.add_unit(Goal, x, y)

    def add_enemy_following_target(self, x, y, hero):
        enemy = self.add_unit(Enemy,  x, y)
        ai = EnemyFollowingTargetAi(hero)
        enemy.add_ai(ai)
        return enemy

    def add_explosion(self, center):
        for u in self.units:
            u.apply_force((u.get_position() - center).normalize())
        self.game_interface.activate_shader_effect(center)
