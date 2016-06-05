def collision_hero_enemy(space, arbiter):
    s1, s2 = arbiter.shapes
    #s1.body.unit.apply_torque()
    #s2.body.unit.apply_torque()
    return True


def collision_hero_border(space, arbiter, game_logic):
    #game_logic.game_ended(player_won=False)
    print 'lose'
    return True


def collision_ball_border(space, arbiter, game_logic):
    s1, s2 = arbiter.shapes
    s1.body.unit.apply_torque()
    s2.body.unit.apply_torque()
    game_logic.on_game_end(player_won=True)
    print 'win'
    return True
