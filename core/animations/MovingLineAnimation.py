from animations.Animation import Animation
from random import random
import colorsys
import time
import Config

class MovingLineAnimation(Animation):

    def __init__(self, frame_callback, beat_event):
        super().__init__(frame_callback, beat_event)
        self.rand = 1
        self.points = []
        self.color = colorsys.hsv_to_rgb(random(), 1, 1)
        self.x1 = 0
        self.y1 = random()
        self.vx1 = random() * 0.02 + 0.015
        self.vy1 = random() * 0.02 + 0.015

        self.x2 = random()
        self.y2 = 0
        self.vx2 = random() * 0.02 + 0.015
        self.vy2 = random() * 0.02 + 0.015


    def change_color(self):
        self.color = colorsys.hsv_to_rgb(random(), 1, 1)

    def loop(self):


        if self.x1 > 1:
            self.vx1 = -self.vx1
            self.change_color()

        if self.x1 < 0:
            self.vx1 = -self.vx1
            self.change_color()

        if self.y1 > 1:
            self.vy1 = -self.vy1
            self.change_color()

        if self.y1 < 0:
            self.vy1 = -self.vy1
            self.change_color()

        if self.x2 > 1:
            self.vx2 = -self.vx2
            self.change_color()

        if self.x2 < 0:
            self.vx2 = -self.vx2
            self.change_color()

        if self.y2 > 1:
            self.vy2 = -self.vy2
            self.change_color()

        if self.y2 < 0:
            self.vy2 = -self.vy2
            self.change_color()


        self.x1 += self.vx1
        self.x2 += self.vx2
        self.y1 += self.vy1
        self.y2 += self.vy2


        frame = []
        for point in self.line_points(self.x1, self.y1, self.x2, self.y2, 90):
            frame = frame + [{'x': point[0], 'y': point[1], 'r': self.color[0], 'g': self.color[1], 'b': self.color[2]}]
        for point in self.line_points(self.x2, self.y2, self.x1, self.y1, 90):
            frame = frame + [{'x': point[0], 'y': point[1], 'r': self.color[0], 'g': self.color[1], 'b': self.color[2]}]

     
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

