from animations.Animation import Animation
import random
import colorsys
import time

class CircleAnimation(Animation):

    def __init__(self, frame_callback, beat_event):
        super().__init__(frame_callback, beat_event)
        self.rand = 1
        self.r = 0.1
        self.color = (1, 1, 1)

    def loop(self):

        frame = []

        if self.beat_event.is_set():
            self.beat_event.clear()

            self.r = 0.1
            self.color = colorsys.hsv_to_rgb(random.random(), 1, 1)

        if self.r < 0.5:
            self.r += 0.02


        for point in self.circle_points(self.r, 200):
            frame = frame + [{'x': point[0] + 0.5, 'y': point[1] + 0.5, 'r': self.color[0], 'g': self.color[1], 'b': self.color[2]}]


        self.frame_callback(frame)

        time.sleep(0.01)

