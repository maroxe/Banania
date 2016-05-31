from kivy.uix.widget import Widget

from core.statemanager import State


class EndLevel(State):
    count = 1

    def __init__(self, player_won):
        self.player_won = player_won

    def build_widget(self):
        self.w = EndLevelWidget()
        self.w.player_won = self.player_won
        b = self.w.continue_button
        def on_button_pressed(instance):
            self.stop()
            self.on_quit()

        b.bind(on_press=on_button_pressed)
        return self.w

    def update(self, dt):
        if not self.is_paused:
            self.count -= dt
            self.w.count = self.count
        if False and self.count < 0:
            self.stop()
            self.on_quit()
        return super(self.__class__, self).update(dt=dt)


class EndLevelWidget(Widget):
    pass
