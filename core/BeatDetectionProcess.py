from multiprocessing import Value, Process
from ctypes import c_bool

import pyaudio
import numpy as np
import aubio

class BeatDetectionProcess:

    def __init__(self, beat_callback):
        self.process = Process(target=self.__run)
        self.request_exit = Value(c_bool, False)
        self.beat_callback = beat_callback

    def __run(self):
        print("Beat Detector Start")

        p = pyaudio.PyAudio()

         # open stream
        buffer_size = 256
        pyaudio_format = pyaudio.paFloat32
        n_channels = 1
        samplerate = 44100
        stream = p.open(format=pyaudio_format,
                        channels=n_channels,
                        rate=samplerate,
                        input=True,
                        frames_per_buffer=buffer_size)

        win_s = buffer_size * 2  # fft size
        hop_s = buffer_size  # hop size

        a_tempo = aubio.tempo("default", win_s, hop_s, samplerate)

        while not self.request_exit.value:
            try:
                audiobuffer = stream.read(buffer_size, exception_on_overflow=False)
                signal = np.fromstring(audiobuffer, dtype=np.float32)

                is_beat = a_tempo(signal)
                if is_beat:
                    # print(is_beat)
                    # print('tick')  # avoid print in audio callback
                    self.beat_callback()

                # print("{} / {}".format(pitch,confidence))
            except:
                print("beatdetector error")

        stream.stop_stream()
        stream.close()
        p.terminate()
        print("Beat Detector Stop")

    def start(self):
        self.process.start()


    def stop(self):
        print("Beat Detector request stop")
        self.request_exit.value = True
        self.process.join()
