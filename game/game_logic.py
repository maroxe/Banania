
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
        self.game_ended = False
        self.stop_when_unpaused = False
        self.i = 0

    def build_widget(self):
        self.game_interface = GameInterface()
        return self.game_interface

    def update(self, dt):
        # continue animation when the game has ended
        if self.is_paused and not self.stop_when_unpaused:
            return True

        self.time += dt
        self.game_interface.score = self.game_state.score
        self.game_interface.time = self.time
        self.game_interface.fps = int((self.i/self.time + 9/dt)/10)
        self.i += 1
        self.event_manager.update(dt)

        self.physics.update(dt)
        for u in self.units:
            u.update(dt)

        if self.is_paused:
            return True

        if self.stop_when_unpaused:
            self.stop()
        return super(GameLogic, self).update(dt=dt)

    def build_level(self, level_file='lvl/level1.lvl'):
        lvl = Level(level_file)
        w, h = lvl.get_header()

        self.game_interface.resize_window(w, h)
        self.physics = Physics(w, h)

        # build units
        hero = self.add_hero(*lvl.units['h'][0])
        ball = self.add_ball(*lvl.units['b'][0])
        goal = self.add_goal(*lvl.units['g'][0])
        units = [hero, ball, goal]
        self.hero, self.ball, self.goal = hero, ball, goal
        for sym, target in [('h', hero), ('b', ball), ('g', goal)]:
            for (x, y) in lvl.units['e%s' % sym]:
                units.append(self.add_enemy_following_target(x, y, target))

        self.units = units

        # build physics space
        self.physics.space.add_collision_handler(
            3,  # goal
            4,  # ball
            post_solve=game_rules.collision_ball_border,
            game_logic=self
        )

        def on_double_tap(dt, pos):
            if not self.is_paused:
                self.add_explosion(hero.get_position())

        self.event_manager.register_action('double tap', on_double_tap)

    def on_game_end(self, player_won):
        self.game_ended = True
        if player_won:
            self.game_state.score += 1
        else:
            self.game_state.score -= 1
        self.game_state.player_won = player_won
        self.goal.set_animation('happy', 2)

    def stop(self):
        self.on_quit()
        super(GameLogic, self).stop()

    # function for building units
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
        self.hero.set_animation('special', 0.3)
        self.goal.set_animation('unhappy', 2)
