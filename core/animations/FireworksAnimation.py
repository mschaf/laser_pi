from animations.Animation import Animation
from random import randrange, random
import colorsys
import time
import math

class FireworksAnimation(Animation):

    def __init__(self, frame_callback, beat_event):
        super().__init__(frame_callback, beat_event)
        self.rand = 1
        self.init()


    def init(self):
        vx = (random() * 0.01) - 0.005
        vy = 0.02 + random() * 0.01
        self.points = [[0.5, 0, 0.07, 0.14, 0, vx, vy]]
        self.phase = 0
        self.i = 0
        self.g = 0.0005
        self.r = 1
        self.t = 1

    def loop(self):
        self.i += 1

        if self.points[0][6] < 0 and self.phase == 0:
            self.phase = 1
            self.i = 0
            self.g = 0.0002
            self.r = 0.95
            color = colorsys.hsv_to_rgb(random() , 1, 1)

            f = 0.03
            f2 = 0.01
            f3 = 0.01 * (random() * 0.5 + 0.5)
            case = randrange(0, 3)
            n = 10

            for i in range(10):
                vx = 0
                vy = 0

                if case == 0:
                    vx = random()*f-f/2
                    vy = random()*f-f/2
                    
                elif case == 1:
                    vx = random()*f2-f2/2 + self.points[0][5]
                    vy = random()*f2*0.7+0.01

                elif case == 2:
                    rr = (random() * 0.1 + 0.9)
                    vx = math.cos(2*math.pi/n*i)*f3 * rr
                    vy = math.sin(2*math.pi/n*i )*f3 * rr

                self.points.append([self.points[0][0], self.points[0][1], color[0], color[1], color[2], vx, vy])
            
            self.points.pop(0)

        if self.phase == 1:
            for i in range(len(self.points)):
                self.t -= 0.0005
                self.points[i][2] *= self.t
                self.points[i][3] *= self.t
                self.points[i][4] *= self.t

        if self.i > 30 and self.phase == 1:
            self.init()

        for i in range(len(self.points)):
            self.points[i][6] -= self.g # gravity

            self.points[i][5] *= self.r # air resitance
            self.points[i][6] *= self.r

            self.points[i][0] += self.points[i][5]
            self.points[i][1] += self.points[i][6]


        frame = []

        for i in range(len(self.points)):
            point = self.points[i]
            next_point = self.points[(i + 1) % len(self.points)]

            frame = frame + [{'x': point[0], 'y': point[1], 'r': 0, 'g': 0, 'b': 0}] * 10
            frame = frame + [{'x': point[0], 'y': point[1], 'r': point[2], 'g': point[3], 'b': point[4]}] * 20
            # frame = frame + self.line_frame(point[0], point[1], next_point[0], next_point[1], 1, 0, 0, 0)

        self.frame_callback(frame)

        time.sleep(0.02)
