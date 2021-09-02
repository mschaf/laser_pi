from animations.Animation import Animation
import random
import colorsys
import time
import Config

class SweepingFanAnimation(Animation):

    def __init__(self, frame_callback, beat_event):
        super().__init__(frame_callback, beat_event)
        self.rand = 1
        self.points = []
        self.color = colorsys.hsv_to_rgb(random.random(), 1, 1)
        self.x1 = 0.4
        self.x2 = 0.6
        self.v1 = 0.01
        self.v2 = -0.01
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

            self.color = colorsys.hsv_to_rgb(random.random(), 1, 1)

        
        self.x1 += self.v1
        self.x2 += self.v2

        if self.x1 > 1:
            self.v1 = random.random() * -0.1 - 0.01
            self.x1 += self.v1

        if self.x1 < 0:
            self.v1 = random.random() * 0.1 + 0.01
            self.x1 += self.v1

        if self.x2 > 1:
            self.v2 = random.random() * -0.1 - 0.01
            self.x2 += self.v2

        if self.x2 < 0:
            self.v2 = random.random() * 0.1 + 0.01
            self.x2 += self.v2


        frame = self.line_frame(self.x1, Config.line_animation_height(), self.x2, Config.line_animation_height(), 200, self.color[0], self.color[1], self.color[2])

        # self.points = self.line_points()

        # frame = []

        # for i in range(len(self.points)*2-2):
        #     point = self.points[self.ii(i)]
        #     next_point = self.points[self.ii(i + 1)]

        #     frame = frame + [{'x': point[0], 'y': point[1], 'r': 0, 'g': 0, 'b': 0}] * 5
        #     frame = frame + [{'x': point[0], 'y': point[1], 'r': self.color[0], 'g': self.color[1], 'b': self.color[2]}] * 15
        #     # frame = frame + self.line_frame(point[0], point[1], next_point[0], next_point[1], 1, 0, 0, 0)

        self.frame_callback(frame)

        time.sleep(0.02)

