from kivy.uix.widget import Widget

from core.statemanager import State
from core import config


class MenuState(State):

    def __init__(self, *args, **kwargs):
        super(MenuState, self).__init__(*args, **kwargs)

    def update(self, dt, **kwargs):
        self.widget.active = not self.is_paused
        return super(MenuState, self).update(dt=dt)

    def on_stop(self):
        self.on_quit()
        super(MenuState, self).on_stop()


class MenuWidget(Widget):
    scale = config.get_scale_object().get
