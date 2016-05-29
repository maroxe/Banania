from kivy.uix.widget import Widget
from kivy.uix.button import Button

from core.statemanager import State


class StartMenu(State):

    def build_widget(self):
        w = StartMenuWidget()
        b = w.start_button

        def on_button_pressed(instance):
            self.stop()
            self.on_quit()

        b.bind(on_press=on_button_pressed)
        return w


class StartMenuWidget(Widget):
    pass
