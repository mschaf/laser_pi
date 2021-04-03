from multiprocessing import Value, Process, Event
from ctypes import c_bool
from animations.SweepAnimation import SweepAnimation
from animations.PointsAnimation import PointsAnimation
from animations.ThunderStormAnimation import ThunderStormAnimation
from animations.CircleAnimation import CircleAnimation
from AnimationManager import AnimationManager

class AnimationProcess:


    def __init__(self, frame_callback):
        self.process = Process(target=self.__run)
        self.request_exit = Value(c_bool, False)
        self.beat_event = Event()
        self.frame_callback = frame_callback
        self.current_animation = None
        self.animation_manager = AnimationManager()

    def __run(self):
        print("Animation Process start")
        while not self.request_exit.value:
            new_animation_class = self.animation_manager.determine_animation_class()
            if new_animation_class:
                self.current_animation = new_animation_class(self.frame_callback, self.beat_event)

            if self.current_animation:
                self.current_animation.loop()

        print("Animation Process stopped")


    def beat(self):
        print("beat requested")
        if self.beat_event.is_set():
            print("Warning, beat requested while previous hasn´t been cleared")

        self.beat_event.set()

    def start(self):
        self.process.start()


    def stop(self):
        print("Animation Process request stop")
        self.request_exit.value = True
        self.process.join()    
