from kivy.uix.button import Button

from core.statemanager import State


class Pause(State):

    def build_widget(self):
        b = Button(text='Hello world', font_size=14)

        def on_button_pressed(instance):
            print 'button pressed'
            self.stop()
            self.on_quit()

        b.bind(on_press=on_button_pressed)
        return b
