from animations.Animation import Animation
import random
import colorsys
import time
import math
import random

class RGBDeathRayAnimation(Animation):

    def __init__(self, frame_callback, beat_event):
        super().__init__(frame_callback, beat_event)
        self.rand = 1
        self.r = 0
        self.track = []
        self.t = [0.1, 0.1]
        self.l = [0, 0]
        self.p = [0, 0]
        self.color = colorsys.hsv_to_rgb(random.random(), 1, 1)

    def loop(self):

        frame = []

        if self.beat_event.is_set():
            self.beat_event.clear()
            self.t = self.p
            self.track = []

        if len(self.track) == 1:
            print("overflow")


        if len(self.track) == 0:
            self.color = colorsys.hsv_to_rgb(random.random(), 1, 1)
            self.l = self.t

            dist = 0
            
            while dist < 0.6:
                self.t = [random.uniform(0,1), random.uniform(0,0.7)]
                dist = math.sqrt( abs(self.t[0] - self.l[0])**2 +  abs(self.t[1] - self.l[1]**2 ))
            
            self.track = self.line_points(self.l[0], self.l[1], self.t[0], self.t[1], int(dist * 50))


        self.p = self.track.pop(0)

        frame =  [{'x': self.p[0], 'y': self.p[1], 'r': self.color[0], 'g': self.color[1], 'b': self.color[2]}]


        self.frame_callback(frame)

        time.sleep(0.01)

