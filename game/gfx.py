from kivy.core.window import Window as KivyWindow
from kivy.uix.widget import Widget
from kivy.uix.scatter import Scatter
from kivy.clock import Clock

from core import config


class Window(Scatter):
    """
    Root widget for GameApp
    """

    def __init__(self, *args, **kwargs):
        kwargs.setdefault('size_hint', (None, None))
        kwargs.setdefault('do_scale', False)
        kwargs.setdefault('do_translation', False)
        kwargs.setdefault('do_rotation', False)

        super(Window, self).__init__(*args, **kwargs)
        Clock.schedule_once(self.fit_to_window, -1)
        KivyWindow.bind(system_size=self.on_window_resize)

    def on_window_resize(self, window, size):
        self.fit_to_window()

    def fit_to_window(self, *args):
        self.scale = min(KivyWindow.height/float(self.height),
                         KivyWindow.width/float(self.width))
        self.center = KivyWindow.center
        for c in self.children:
            pass
            #c.size = self.size

    def on_touch_down(self, touch, *args):
        self.event_manager.on_touch_down(touch, *args)
        return super(self.__class__, self).on_touch_down(touch, *args)

    # send events to event manager
    def on_touch_up(self, touch, *args):
        self.event_manager.on_touch_up(touch)
        return super(self.__class__, self).on_touch_up(touch, *args)

    def take_screenshot(self, filename):
        KivyWindow.screenshot(name=filename)


class UnitGfx(Widget):

    def __init__(self, size, *args, **kargs):
        self.scale = config.get_scale_object()
        self.size = self.scale.get(*size)
        super(UnitGfx, self).__init__(*args, **kargs)
        self.set_animation()
        self.count = 0

    def set_position(self, x, y):
        self.pos = self.scale.get(x, y)

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
