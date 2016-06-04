from kivy.uix.widget import Widget
from core.statemanager import State


class GameState(State):

    score = 0

    def __init__(self, levels_file, *args):
        super(self.__class__, self).__init__(*args)
        self.reset()
        self.levels = open(levels_file).read().strip().split('\n')
        self.current_level = len(self.levels)

    def build_widget(self):
        self.root_widget = Widget()
        return self.root_widget

    def update(self, dt):
        return True

    def advance_level(self):
        self.current_level += 1
        if self.current_level >= len(self.levels):
            return None
        return self.levels[self.current_level]

    def reset(self):
        self.current_level = -1
