from BeatDetectionProcess import BeatDetectionProcess
from time import sleep


def beat_callback():
    print("Beat")


beat_detection_process = BeatDetectionProcess(beat_callback=beat_callback)
beat_detection_process.start()
sleep(30)
beat_detection_process.stop()