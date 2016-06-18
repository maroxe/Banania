class GameRules(object):

    def __init__(self, game_logic):
        self.game_logic = game_logic

    def collision_hero_enemy(self, space, arbiter):
        s1, s2 = arbiter.shapes
        s1.body.data.apply_torque()
        s2.body.data.apply_torque()
        return True

    def collision_hero_border(self, space, arbiter):
        self.game_logic.game_ended(player_won=False)
        print 'lose'
        return True

    def collision_ball_border(self, space, arbiter):
        s1, s2 = arbiter.shapes
        s1.body.data.apply_torque()
        s2.body.data.apply_torque()

        self.game_logic.on_game_end(player_won=True)
        print 'win'
        return True
