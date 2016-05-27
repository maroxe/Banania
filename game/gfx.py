from kivy.uix.widget import Widget
from kivy.vector import Vector


class Window(Widget):

    def resize(self, w, h):
        from kivy.core.window import Window
        Window.size = (w, h)

    # send events to event manager
    def on_touch_up(self, touch):
        self.event_manager.on_touch_up(touch)


class UnitGfx(Widget):

    def set_position(self, x, y):
        self.pos = Vector(x, y)

    def set_animation(self, anim):
        # TODO: move this to config file
        animations = {
            'up': self.walkup,
            'down': self.walkdown,
            'left': self.walkleft,
            'right': self.walkright
        }

        self.source = animations[anim]


class HeroGfx(UnitGfx):
    pass


class EnemiGfx(UnitGfx):
    pass


class BrickGfx(UnitGfx):
    pass
