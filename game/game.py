from kivy.app import App
from kivy.clock import Clock

from core.statemanager import StateManager
from game_logic import GameLogic
from game_state import GameState
from gfx import Window

from ui.start_menu import StartMenu
from ui.begin_level import BeginLevel
from ui.end_level import EndLevel


class GameApp(App):

    def build(self):
        self.state_mgr = StateManager()
        self.window = Window()
        Clock.schedule_interval(self.update, 1.0/60.0)

        self.game_state = GameState()

        self.state_mgr.push_state(self.game_state)
        self.start_new_game()
        self.add_graphic_state(StartMenu())

        return self.window

    def start_new_game(self):
        game_logic = GameLogic()
        game_logic.game_state = self.game_state
        self.window.event_manager = game_logic.event_manager
        self.add_graphic_state(game_logic)
        game_logic.build_level()
        self.add_graphic_state(BeginLevel())
        self.game_logic = game_logic

    def update(self, dt):
        self.state_mgr.update(dt=dt)
        if self.game_logic.is_stopped:
            self.start_new_game()
            self.add_graphic_state(EndLevel(self.game_state.player_won))

    def add_graphic_state(self, state):
        state_gfx = state.build_widget()
        self.window.add_widget(state_gfx)
        self.state_mgr.push_state(state)

        def on_quit():
            self.window.remove_widget(state_gfx)

        state.on_quit = on_quit
