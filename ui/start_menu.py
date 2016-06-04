from menu_state import MenuState, MenuWidget


class StartMenu(MenuState):

    def build_widget(self):
        self.widget = StartMenuWidget()
        b = self.widget.start_button

        def on_button_pressed(instance):
            self.stop()

        b.bind(on_press=on_button_pressed)
        return self.widget


class StartMenuWidget(MenuWidget):
    pass
