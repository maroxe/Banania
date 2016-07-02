from kivy.uix.widget import Widget
from kivy.base import EventLoop
from kivy.clock import Clock
from kivy.graphics import RenderContext

from core import config


class GameInterfaceBackground(Widget):
    pass


class GameInterface(Widget):
    def __init__(self, *kwargs):
        # We must do this, if no other widget has been loaded the
        # GL context may not be fully prepared
        EventLoop.ensure_window()
        # Most likely you will want to use the parent projection
        # and modelviev in order for your widget to behave the same
        # as the rest of the widgets
        self.canvas = RenderContext(use_parent_projection=True,
                                    use_parent_modelview=True)
        self.canvas.shader.source = 'shaders/flame.glsl'
        Clock.schedule_interval(self.update_shader, 0)
        self.effects = {}

        self.count = 0.
        self.center = (0, 0)
        self.scale_obj = config.get_scale_object()
        super(self.__class__, self).__init__(*kwargs)

    def update_shader(self, dt):
        s = self.canvas
        s['time'] = self.count
        s['resolution'] = list(map(float, self.size))
        s['center'] = list(map(float, self.center))
        s['shockParams'] = [10., 0.8, 0.1]
        if self.count > 0:
            self.count -= dt
        self.canvas['is_active'] = self.count

    def activate_shader_effect(self, center):
        self.count = 0.3
        self.center = (center[0] / self.size[0], 1-center[1] / self.size[1])
