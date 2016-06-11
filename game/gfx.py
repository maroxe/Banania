from kivy.uix.widget import Widget
from kivy.vector import Vector


class Window(Widget):

    def resize(self, w, h):
        from kivy.core.window import Window
        Window.size = (w, h)

    def on_touch_down(self, touch, *args):
        self.event_manager.on_touch_down(touch, *args)
        return super(self.__class__, self).on_touch_down(touch, *args)

    # send events to event manager
    def on_touch_up(self, touch, *args):
        self.event_manager.on_touch_up(touch)
        return super(self.__class__, self).on_touch_up(touch, *args)


class UnitGfx(Widget):

    def __init__(self, *args, **kargs):
        super(UnitGfx, self).__init__(*args, **kargs)
        self.set_animation()
        self.count = 0

    def set_position(self, x, y):
        self.pos = Vector(x, y)

    def update(self, dt):
        if not self.count:
            return
        if self.count < 0:
            self.set_animation()
        else:
            self.count -= dt

    def set_rotation(self, angle):
        self.angle = angle

    def set_animation(self, anim='default', duration=None):
        self.count = duration
        self.source = self.animations[anim]


class HeroGfx(UnitGfx):
    pass


class EnemyGfx(UnitGfx):
    pass


class BrickGfx(UnitGfx):
    pass


class GoalGfx(UnitGfx):
    def __init__(self, *args, **kargs):
        super(GoalGfx, self).__init__(*args, **kargs)

