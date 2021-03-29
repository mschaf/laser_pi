import time
import threading
import math
from time import sleep
from Helios import Helios
import random
import colorsys
import multiprocessing

class LaserProcess:

    def __init__(self):
        self.process = multiprocessing.Process(target=self.__run)
        self.helios = Helios()
        self.request_exit = multiprocessing.Value('i', 0)
        self.queue_sweep = multiprocessing.Value('i', 0)
        self.frame_buffer_a = RawArray

    def display_frame(self, frame):


    def __run(self):
        print("Helios open")
        self.helios.open()

        rand = 0
        while not self.request_exit.value:
            if self.queue_sweep.value:
                self.queue_sweep.value = False
                print("sweep")

                rand += 1
                if rand == 4:
                    rand = 0
                n = 75
                r,g,b = colorsys.hsv_to_rgb(random.random(), 1, 1)
                #r,g,b = 1, 0, 1
                num_points = 20
                

                for i in range(n):
                    p = (1.0 / n) * i

                    frame = None
                    if rand == 2:
                        frame = self.line_frame(p, 0, p, 1, num_points, r, g, b)
                    if rand == 0:
                        frame = self.line_frame(1-p, 0, 1-p, 1, num_points, r, g, b)
                    if rand == 1:
                        frame = self.line_frame(0, p, 1, p, num_points, r, g, b)
                    if rand == 3:
                        frame = self.line_frame(0, 1-p, 1, 1-p, num_points, r, g, b)
                            
                    self.helios.send_frame(frame)
                self.helios.send_frame([{ 'x': 0, 'y': 0, 'r': 0, 'g': 0, 'b': 0}] )

        print("Helios close")
        self.helios.close()

    def start(self):
       self.process.start()

    def sweep(self):
        self.queue_sweep.value = True

    def stop(self):
        self.request_exit.value = True
        self.process.join()

    