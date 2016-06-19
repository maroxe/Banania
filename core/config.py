from kivy.core.window import Window as KivyWindow
from kivy.metrics import dp
from math import Vector2d as v


def get_window_size():
    return v(KivyWindow.size) 


def get_dp():
    return dp(1)


def get_sprite_size():
    return (10., 10.)
