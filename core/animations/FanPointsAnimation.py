from animations.Animation import Animation
import random
import colorsys
import time

class FanPointsAnimation(Animation):

    def __init__(self, frame_callback, beat_event):
        super().__init__(frame_callback, beat_event)
        self.rand = 1
        self.points = []
        self.color = colorsys.hsv_to_rgb(random.random(), 1, 1)
        self.w = 0.01
        for i in range(11):
            self.points += [(0.5, 0.5)]

    def ii(self, i):
        i = i % (len(self.points)*2-2)
        if i >= len(self.points):
            i = i - (i % len(self.points)) * 2 - 2

        return(i)

    def loop(self):

        if self.beat_event.is_set():
            self.beat_event.clear()

            self.w = 0.2
            self.color = colorsys.hsv_to_rgb(random.random(), 1, 1)

        if self.w < 0.5:
            self.w += 0.02

        self.points = self.line_points(0.5 - self.w, 0.5, 0.5 + self.w, 0.5, 11)

        frame = []

        for i in range(len(self.points)*2-2):
            point = self.points[self.ii(i)]
            next_point = self.points[self.ii(i + 1)]

            frame = frame + [{'x': point[0], 'y': point[1], 'r': 0, 'g': 0, 'b': 0}] * 5
            frame = frame + [{'x': point[0], 'y': point[1], 'r': self.color[0], 'g': self.color[1], 'b': self.color[2]}] * 15
            # frame = frame + self.line_frame(point[0], point[1], next_point[0], next_point[1], 1, 0, 0, 0)

        self.frame_callback(frame)

        time.sleep(0.02)

