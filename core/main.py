import math
from time import sleep
from Helios import Helios
import random
from LaserProcess import LaserProcess
from AnimationProcess import AnimationProcess
from BeatDetectionProcess import BeatDetectionProcess

def beat_callback():
    print("Beat")

laser_process = LaserProcess()
animation_process = AnimationProcess(frame_callback=laser_process.display_frame)
beat_detection_process = BeatDetectionProcess(beat_callback=animation_process.beat)

laser_process.start()
animation_process.start()
beat_detection_process.start()

while True:
    try:
        sleep(1)
    except KeyboardInterrupt:
        print("*** Ctrl+C pressed, exiting")
        break

laser_process.stop()
animation_process.stop()
beat_detection_process.stop()