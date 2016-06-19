from kivy.vector import Vector

Vector2d = Vector


class ScaledField:
    """
    Converts metric units from
    [0, 100] x [0, 100] to [0, w] x [0, h]
    """

    def __init__(self, dp, w, h):
        self.dp = dp
        self.size = Vector2d(w, h)

    def get(self, x, y):
        return Vector2d(x, y) / (100., 100.) * self.size

    def get_dp(self, x, y):
        """
        Pixel density independent position
        """

        return self.get(x, y) / self.dp
