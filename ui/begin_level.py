from kivy.uix.widget import Widget

from core.statemanager import State


class BeginLevel(State):
    count = 1

    def build_widget(self):
        self.w = BeginLevelWidget()
        self.w.count = self.count
        return self.w

    def update(self, dt):
        if not self.is_paused:
            self.count -= dt
            self.w.count = self.count
        if self.count < 0:
            self.stop()
            self.on_quit()
        return super(self.__class__, self).update(dt=dt)


class BeginLevelWidget(Widget):
    pass
