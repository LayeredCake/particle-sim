
class Window():
    def __init__(self, surface, w, h, x=0, y=0, zoom=1):
        self.surface = surface
        self.zoom = zoom
        self.w = w
        self.h = h
        self.x = x
        self.y = y