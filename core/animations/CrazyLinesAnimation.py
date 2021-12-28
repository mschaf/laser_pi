from animations.Animation import Animation
from random import random, randrange
import colorsys
import time
import Config
import math

class CrazyLinesAnimation(Animation):

    def __init__(self, frame_callback, beat_event):
        super().__init__(frame_callback, beat_event)
        self.rand = 1
        self.points = []
        self.change_color()
        self.new_points()
        self.i = 0
        

    def new_points(self):
        r = randrange(0, 4)

        if r == 0:
            self.x1 = 0
            self.y1 = random()
        elif r == 1:
            self.x1 = 1
            self.y1 = random()

        elif r == 2:
            self.x1 = random()
            self.y1 = 0

        elif r == 3:
            self.x1 = random()
            self.y1 = 1

        r = randrange(0, 4)

        if r == 0:
            self.x2 = 0
            self.y2 = random()

        elif r == 1:
            self.x2 = 1
            self.y2 = random()

        elif r == 2:
            self.x2 = random()
            self.y2 = 0

        elif r == 3:
            self.x2 = random()
            self.y2 = 1


    def change_color(self):
        self.color = colorsys.hsv_to_rgb(random(), 1, 1)

    def long_new_points(self):
        line_length = 0
        while line_length < 0.5:
            self.new_points()

            dx = max(self.x1, self.x2) - min(self.x1, self.x2)
            dy = max(self.y1, self.y2) - min(self.y1, self.y2)
            line_length = math.sqrt(dx*dx+dy*dy)



    def loop(self):

        self.i += 1
        if self.i > 5:
            self.i = 0
            self.change_color()
            self.long_new_points()

        
        #if self.beat_event.is_set():
        #    self.beat_event.clear()
        #    self.change_color()
        #    self.long_new_points()


        frame = []
        
        for point in self.line_points(self.x1, self.y1, self.x2, self.y2, 70):
            frame = frame + [{'x': point[0], 'y': point[1], 'r': self.color[0], 'g': self.color[1], 'b': self.color[2]}]
        for point in self.line_points(self.x2, self.y2, self.x1, self.y1, 70):
            frame = frame + [{'x': point[0], 'y': point[1], 'r': self.color[0], 'g': self.color[1], 'b': self.color[2]}]
        
        for i in range(10):
            frame = frame + [{'x': self.x1, 'y': self.y1, 'r': 0, 'g': 0, 'b': 0}]


        self.frame_callback(frame)

        time.sleep(0.02)

