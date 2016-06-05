from menu_state import MenuState, MenuWidget


class TemporaryMessage(MenuState):

    def __init__(self, msg='Empty msg', duration=1, *args):
        self.msg = msg
        self.duration = duration

    def build_widget(self):
        self.widget = TemporaryMessageWidget()
        self.widget.msg = self.msg
        self.widget.count = self.duration
        return self.widget

    def update(self, dt):
        if not self.is_paused:
            self.duration -= dt
            self.widget.count = self.duration

        if self.duration < 0:
            self.stop()
            self.on_quit()

        return super(TemporaryMessage, self).update(dt=dt)


class TemporaryMessageWidget(MenuWidget):
    pass
