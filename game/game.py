from kivy.app import App
from kivy.clock import Clock

from core.statemanager import StateManager
from game_logic import GameLogic
from gfx import Window
from pause import Pause


class GameApp(App):

    def build(self):
        self.state_mgr = StateManager()
        self.window = Window()
        Clock.schedule_interval(self.update, 1.0/60.0)

        game_logic = GameLogic()
        self.window.event_manager = game_logic.event_manager
        self.add_graphic_state(game_logic)
        game_logic.build_level()

        self.add_graphic_state(Pause())

        return self.window

    def update(self, dt):
        self.state_mgr.update(dt=dt)

    def add_graphic_state(self, state):
        state_gfx = state.build_widget()
        self.window.add_widget(state_gfx)
        self.state_mgr.push_state(state)

        def on_quit():
            self.window.remove_widget(state_gfx)

        state.on_quit = on_quit
