from kivy.uix.widget import Widget

from menu_state import MenuState, MenuWidget


class EndLevel(MenuState):
    count = 1

    def __init__(self, player_won):
        self.player_won = player_won

    def build_widget(self):
        self.widget = EndLevelWidget()
        self.widget.player_won = self.player_won
        b = self.widget.continue_button

        def on_button_pressed(instance):
            self.stop()
            self.on_quit()

        b.bind(on_press=on_button_pressed)
        return self.widget

    def update(self, dt):
        if not self.is_paused:
            self.count -= dt
            self.widget.count = self.count
        if False and self.count < 0:
            self.stop()
            self.on_quit()
        return super(self.__class__, self).update(dt=dt)


class EndLevelWidget(MenuWidget):
    pass
