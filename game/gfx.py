from kivy.uix.widget import Widget
from kivy.vector import Vector


class Window(Widget):

    def resize(self, w, h):
        from kivy.core.window import Window
        Window.size = (w, h)

    # events
    def on_touch_down(self, touch):
        self.event_manager.on_touch_down()

    def on_touch_up(self, touch):
        self.event_manager.on_touch_up()

    def on_touch_left(self, touch):
        self.event_manager.on_touch_left()

    def on_touch_right(self, touch):
        self.event_manager.on_touch_right()


class UnitGfx(Widget):

    def set_position(self, x, y):
        self.pos = Vector(x, y)

    def set_animation(self, anim):
        self.source = self.animation[anim]


class HeroGfx(UnitGfx):
    pass


class EnemiGfx(UnitGfx):
    pass


class BrickGfx(UnitGfx):
    pass
