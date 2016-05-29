from kivy.uix.widget import Widget
from core.statemanager import State


class GameState(State):

    score = 0

    def build_widget(self):
        self.root_widget = Widget()
        return self.root_widget

    def update(self, dt):
        return True
