from animations.Animation import Animation
import time

class EmptyAnimation(Animation):

    def __init__(self, frame_callback, beat_event):
        super().__init__(frame_callback, beat_event)
        self.rand = 1

    def loop(self):
        self.frame_callback([{'x': 0.5, 'y': 0.5, 'r': 0, 'g': 0, 'b': 0}])
        time.sleep(0.1)


