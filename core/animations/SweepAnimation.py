from Animation import Animation
import random
import colorsys

class SweepAnimation(Animation):

    def __init__(self, frame_callback, do_beat):
        super().__init__(frame_callback, do_beat)
        self.rand = 1

    def loop(self):
        if self.do_beat.value:
            self.do_beat.value = False
            print("sweep")

            self.rand += 1
            if self.rand == 4:
                self.rand = 0
            n = 75
            r, g, b = colorsys.hsv_to_rgb(random.random(), 1, 1)
            # r,g,b = 1, 0, 1
            num_points = 20

            for i in range(n):
                p = (1.0 / n) * i

                frame = None
                if self.rand == 2:
                    frame = self.line_frame(p, 0, p, 1, num_points, r, g, b)
                if self.rand == 0:
                    frame = self.line_frame(1 - p, 0, 1 - p, 1, num_points, r, g, b)
                if self.rand == 1:
                    frame = self.line_frame(0, p, 1, p, num_points, r, g, b)
                if self.rand == 3:
                    frame = self.line_frame(0, 1 - p, 1, 1 - p, num_points, r, g, b)

                self.frame_callback(frame)
            self.frame_callback([{'x': 0, 'y': 0, 'r': 0, 'g': 0, 'b': 0}])



