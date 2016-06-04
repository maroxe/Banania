from kivy.app import App
from kivy.clock import Clock

from core.statemanager import StateManager, State
from game_logic import GameLogic
from game_state import GameState
from gfx import Window

from ui.start_menu import StartMenu
from ui.end_level import EndLevel
from ui.temporary_msg import TemporaryMessage


class GameApp(App):

    def build(self):
        self.state_mgr = StateManager()
        self.window = Window()
        Clock.schedule_interval(self.update, 1.0/60.0)

        self.game_state = GameState('lvl/levels')

        self.state_mgr.push_state(self.game_state)
        self.state_mgr.push_state(GameCreatorState(self))

        return self.window

    def start_new_game(self):
        next_lvl = self.game_state.advance_level()

        # if we finished all the levels
        restart_game = False
        if not next_lvl:
            self.game_state.reset()
            next_lvl = self.game_state.advance_level()
            restart_game = True

        # create new game
        game_logic = GameLogic()
        game_logic.game_state = self.game_state
        self.window.event_manager = game_logic.event_manager
        self.add_graphic_state(game_logic)
        game_logic.build_level(next_lvl)
        self.game_logic = game_logic

        # Display message at the begining of each level
        msg = 'Level %d' % self.game_state.current_level
        self.add_graphic_state(TemporaryMessage(msg))

        if restart_game:
            self.add_graphic_state(StartMenu())
        else:
            self.add_graphic_state(EndLevel(True))

    def update(self, dt):
        self.state_mgr.update(dt=dt)
        if self.game_logic.game_ended:
            # if this is the first time after the game has ended
            if not self.game_logic.stop_when_unpaused:
                display_msg = TemporaryMessage('GOOAAALL!!', duration=2)
                self.add_graphic_state(display_msg)
                self.game_logic.stop_when_unpaused = True

    def add_graphic_state(self, state):
        state_gfx = state.build_widget()
        self.window.add_widget(state_gfx)
        self.state_mgr.push_state(state)

        def on_quit():
            self.window.remove_widget(state_gfx)

        state.on_quit = on_quit


class GameCreatorState(State):
    """
    A state whose sole responsability is to create 
    a game when unpaused.
    """
    def __init__(self, game_app):
        self.game_app = game_app

    def update(self, dt):
        if not self.is_paused:
            self.game_app.start_new_game()
