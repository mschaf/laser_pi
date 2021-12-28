from animations.Animation import Animation
from random import random
import colorsys
import time
import math
import Config

class FlippingLineAnimation(Animation):

    def __init__(self, frame_callback, beat_event):
        super().__init__(frame_callback, beat_event)
        self.mode = 0
        self.angle = 0
        self.color = colorsys.hsv_to_rgb(random(), 1, 1)
        self.target_color = colorsys.hsv_to_rgb(random(), 1, 1)
        self.change_color()

    def change_color(self):
        self.color = self.target_color

        color_distance = 0

        while color_distance < 0.3:
            self.target_color = colorsys.hsv_to_rgb(random(), 1, 1)
            dr = self.target_color[0] - self.color[0]
            dg = self.target_color[1] - self.color[1]
            db = self.target_color[2] - self.color[2]

            color_distance = math.sqrt(dr*dr+dg*dg+db*db)

    def loop(self):

        x1 = 0
        y1 = 0

        self.angle += 0.02
        if self.angle > 1:
            self.angle = 0
            self.mode += 1
            self.change_color()
            if self.mode > 3:
                self.mode = 0


        dr = self.target_color[0] - self.color[0]
        dg = self.target_color[1] - self.color[1]
        db = self.target_color[2] - self.color[2]

        r = self.color[0] + dr * self.angle
        g = self.color[1] + dg * self.angle
        b = self.color[2] + db * self.angle
 


        if self.mode == 0:
            x1 = 0
            y1 = 0
            x2 = math.cos(0.5*math.pi*self.angle)
            y2 = math.sin(0.5*math.pi*self.angle)


        elif self.mode == 1:
            x1 = 0
            y1 = 1
            x2 = math.cos(0.5*math.pi*(1-self.angle))
            y2 = 1- math.sin(0.5*math.pi*(1-self.angle))


            
        elif self.mode == 2:
            x1 = 1
            y1 = 1
            x2 = 1-math.cos(0.5*math.pi*self.angle)
            y2 = 1-math.sin(0.5*math.pi*self.angle)

            
        elif self.mode == 3:
            x1 = 1
            y1 = 0
            x2 = 1-math.cos(0.5*math.pi*(1-self.angle))
            y2 = math.sin(0.5*math.pi*(1-self.angle))

        frame = []
        for point in self.line_points(x1, y1, x2, y2, 60):
            frame = frame + [{'x': point[0], 'y': point[1], 'r': r, 'g': g, 'b': b}]
        for point in self.line_points(x2, y2, x1, y1, 60):
            frame = frame + [{'x': point[0], 'y': point[1], 'r': r, 'g': g, 'b': b}]

     
        # self.points = self.line_points()

        # frame = []

        # for i in range(len(self.points)*2-2):
        #     point = self.points[self.ii(i)]
        #     next_point = self.points[self.ii(i + 1)]

        #     frame = frame + [{'x': point[0], 'y': point[1], 'r': 0, 'g': 0, 'b': 0}] * 5
        #     frame = frame + [{'x': point[0], 'y': point[1], 'r': self.color[0], 'g': self.color[1], 'b': self.color[2]}] * 15
        #     # frame = frame + self.line_frame(point[0], point[1], next_point[0], next_point[1], 1, 0, 0, 0)

        self.frame_callback(frame)

        time.sleep(0.01)

