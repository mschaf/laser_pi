from multiprocessing import Value, Process
from ctypes import c_bool
from animations.SweepAnimation import SweepAnimation


class AnimationProcess:

    def __init__(self, laser_process):
        self.process = Process(target=self.__run)
        self.request_exit = Value(c_bool, False)
        self.request_beat = Value(c_bool, False)
        self.laser_process = laser_process
        self.current_animation = SweepAnimation(frame_callback=self._frame_callback, do_beat=self.request_beat)

    def __run(self):
        while not self.request_exit:
            if self.current_animation:
                self.current_animation.loop()

    def _frame_callback(self, frame):
        self.laser_process.display_frame(frame)

    def beat(self):
        if self.request_beat:
            print("Warning, beat overflow")

        self.request_beat.value = True

    def start(self):
        self.process.start()

    def stop(self):
        self.request_exit.value = True
        self.process.join()    
