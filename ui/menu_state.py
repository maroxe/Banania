from kivy.uix.widget import Widget

from core.statemanager import State


class MenuState(State):

    def update(self, dt, **kwargs):
        self.widget.active = not self.is_paused
        return super(MenuState, self).update(dt=dt)

    def on_stop(self):
        self.on_quit()
        super(MenuState, self).on_stop()


class MenuWidget(Widget):
    pass
