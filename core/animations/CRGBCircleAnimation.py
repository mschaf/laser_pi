from animations.Animation import Animation
import random
import colorsys
import time
import math

class CRGBCircleAnimation(Animation):

    def __init__(self, frame_callback, beat_event):
        super().__init__(frame_callback, beat_event)
        self.rand = 1
        self.r = 0

    def loop(self):

        frame = []

        if self.beat_event.is_set():
            self.beat_event.clear()

        if self.r < 1:
            self.r += 0.02
        else:
            self.r = 0


        i = 0.0
        points  = 200

        for point in self.circle_points((math.sin(self.r * 3.14) / 4) + 0.25, points):
            i += 1.0 / points
            color = colorsys.hsv_to_rgb((i + self.r) % 1.0 , 1, 1)
            frame = frame + [{'x': point[0] + 0.5, 'y': point[1] + 0.5, 'r': color[0], 'g': color[1], 'b': color[2]}]


        self.frame_callback(frame)

        time.sleep(0.01)

