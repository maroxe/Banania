import game_rules
from core.statemanager import State
from ui.game_interface import GameInterface
from physics import Physics
from ai import EnemyFollowingTargetAi
from events import EventManager
from units import Hero, Enemy, Brick
from level import Level


class GameLogic(State):

    def __init__(self):
        self.event_manager = EventManager()

    def build_widget(self):
        self.root_widget = GameInterface()
        return self.root_widget

    def update(self, dt):
        self.root_widget.score = self.game_state.score
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
        self.root_widget.size = (w, h)
        self.physics = Physics(w, h)
        hero = self.add_hero(100, 500)
        ball = self.add_ball(200, 100)
        old = self.add_enemy_following_target(0, 400, hero)
        units = [hero, ball, old]
        for i in range(3):
            units.append(self.add_enemy_following_target(i*30, 400, ball))

        for i in range(5, 7):
            new = self.add_enemy_following_target(i*30, 400, old)
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
        self.root_widget.add_widget(u.gfx)
        return u

    def add_hero(self, x, y):
        hero = self.add_unit(Hero, x, y)
        self.event_manager.register_action('swipe', hero.move)
        return hero

    def add_ball(self, x, y):
        return self.add_unit(Brick, x, y)

    def add_enemy_following_target(self, x, y, hero):
        enemy = self.add_unit(Enemy,  x, y)
        ai = EnemyFollowingTargetAi(hero)
        enemy.add_ai(ai)
        return enemy
