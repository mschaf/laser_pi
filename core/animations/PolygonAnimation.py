from animations.Animation import Animation
import random
import colorsys
import time
import math

class PolygonAnimation(Animation):

    def __init__(self, frame_callback, beat_event):
        super().__init__(frame_callback, beat_event)
        self.rand = 1
        self.r = 0.1
        self.rotation = 0
        self.edges = int(random.random() * 3) + 3
        self.colors = [0] * self.edges
        offset = random.random() / self.edges
        for i in range(self.edges):
            self.colors[i] = colorsys.hsv_to_rgb((1 / self.edges) * i + offset, 1, 1)

    def loop(self):

        if self.beat_event.is_set():
            self.beat_event.clear()


        if self.r < 1:
            self.r += 0.01
        else:
            self.r = 0


        self.rotation += 0.01

        if self.rotation > 6.28:
            self.rotation = 0
        
        frame = []

        cirlce_points = self.circle_points((math.sin(self.r * 3.14) / 4) + 0.25, self.edges, self.rotation)

        for i in range(len(cirlce_points)):

            color = self.colors[i %  self.edges]

            for point in self.line_points_a(cirlce_points[i], cirlce_points[(i+1) % len(cirlce_points)], 30):
                frame = frame + [{'x': point[0] + 0.5, 'y': point[1] + 0.5, 'r': color[0], 'g': color[1], 'b': color[2]}]


        self.frame_callback(frame)

        time.sleep(0.01)

