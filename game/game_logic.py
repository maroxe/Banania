from game_rules import GameRules
from core import config
from core.statemanager import State
from ui.game_interface import GameInterface
from physics import Physics
from ai import EnemyFollowingTargetAi
from units import Hero, Enemy, Brick, Goal
from level import Level


class GameLogic(State):

    time = 0

    def __init__(self):
        self.game_ended = False
        self.stop_when_unpaused = False
        self.explosions_left = 3
        self.game_rules = GameRules(self)
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
        self.game_interface.explosions_left = self.explosions_left
        if self.i % 100 == 0:
            self.game_interface.fps = int((self.i/self.time + 9/dt)/10)
        self.i += 1

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
        w, h = 100., 100.
        self.physics = Physics(w, h)

        # build units
        hero = self.add_hero(*lvl.units['h'][0])
        ball = self.add_ball(*lvl.units['b'][0])
        goal = self.add_goal(*lvl.units['g'][0])
        units = [hero, ball, goal]
        self.hero, self.ball, self.goal = hero, ball, goal
        for sym, target, anim in [('h', hero, 'type1'), ('b', ball, 'type2'), ('g', goal, 'type3')]:
            for (x, y) in lvl.units['e%s' % sym]:
                u = self.add_enemy_following_target(x, y, target)
                u.set_animation(anim)
                units.append(u)

        self.units = units

        # build physics space
        self.physics.space.add_collision_handler(
            3,  # goal
            4,  # ball
            post_solve=self.game_rules.collision_ball_border,
        )

        # Bind events to actions
        def on_double_tap(dt, pos):
            if not self.is_paused:
                self.add_explosion(hero.get_position())

        def on_key_down(dt, key):
            actions = {
                'w': self.hero.move_up,
                's': self.hero.move_down,
                'a': self.hero.move_left,
                'd': self.hero.move_right,
                'o': lambda _: self.add_explosion(hero.get_position()),
            }
            if key in actions:
                actions[key](dt)

        self.event_manager.register_action('double tap', on_double_tap)
        self.event_manager.register_action('swipe', self.hero.move)
        self.event_manager.register_action('key down', on_key_down)

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
        size = config.get_sprite_size()
        u = unit_factory(size)
        u.set_position(x, y)
        self.physics.add_body(u)
        self.game_interface.add_widget(u.gfx)
        return u

    def add_hero(self, x, y):
        return self.add_unit(Hero, x, y)

    def add_ball(self, x, y):
        return self.add_unit(Brick, x, y)

    def add_goal(self, x, y):
        return self.add_unit(Goal, x, y)

    def add_enemy_following_target(self, x, y, hero):
        enemy = self.add_unit(Enemy,  x, y)
        ai = EnemyFollowingTargetAi(hero)
        enemy.add_ai(ai)
        return enemy

    # Actions

    def add_explosion(self, center):
        if self.explosions_left <= 0:
            return

        self.explosions_left -= 1
        for u in self.units:
            r = 2e-2 * max(1, (u.get_position() - center).length())
            u.apply_force((u.get_position() - center).normalize() / r)
        self.game_interface.activate_shader_effect(center)
        self.hero.set_animation('special', 3)
        self.goal.set_animation('unhappy', 2)

    def move_hero(self, dt, direction):
        self.hero.move(dt, directly)
