from animations.Animation import Animation
import random
import colorsys
import time

class RGBThunderStormAnimation(Animation):

    def __init__(self, frame_callback, beat_event):
        super().__init__(frame_callback, beat_event)
        self.rand = 1
        self.points = []

    def loop(self):


        self.points = []

        for i in range(10):
            self.points += [(random.random(), random.random())]

        frame = []

        for i in range(len(self.points)):
            point = self.points[i]
            next_point = self.points[(i + 1) % len(self.points)]

            color = colorsys.hsv_to_rgb(random.random(), 1, 1)

            frame = frame + [{'x': point[0], 'y': point[1], 'r': 0, 'g': 0, 'b': 0}] * 10
            frame = frame + [{'x': point[0], 'y': point[1], 'r': color[0], 'g': color[1], 'b': color[2]}] * 30
            # frame = frame + self.line_frame(point[0], point[1], next_point[0], next_point[1], 1, 0, 0, 0)

        self.frame_callback(frame)

        time.sleep(0.02)

