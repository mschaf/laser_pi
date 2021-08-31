from animations.Animation import Animation
import random
import colorsys
import time

class StroboFanAnimation(Animation):

    def __init__(self, frame_callback, beat_event):
        super().__init__(frame_callback, beat_event)
        self.rand = 1
        self.points = []
        self.on = True
        for i in range(11):
            self.points += [(0.5, 0.5)]


    def loop(self):

        if self.beat_event.is_set():
            self.beat_event.clear()

            
        self.on = not self.on

        if self.on:
            self.color = colorsys.hsv_to_rgb(0 , 0, 1)
        else:
            self.color = colorsys.hsv_to_rgb(0 , 0, 0)


        frame = self.line_frame(0, 0.5, 1, 0.5, 100, self.color[0], self.color[1], self.color[2])

        # self.points = self.line_points()

        # frame = []

        # for i in range(len(self.points)*2-2):
        #     point = self.points[self.ii(i)]
        #     next_point = self.points[self.ii(i + 1)]

        #     frame = frame + [{'x': point[0], 'y': point[1], 'r': 0, 'g': 0, 'b': 0}] * 5
        #     frame = frame + [{'x': point[0], 'y': point[1], 'r': self.color[0], 'g': self.color[1], 'b': self.color[2]}] * 15
        #     # frame = frame + self.line_frame(point[0], point[1], next_point[0], next_point[1], 1, 0, 0, 0)

        self.frame_callback(frame)

        time.sleep(0.05)

