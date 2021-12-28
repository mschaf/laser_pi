from multiprocessing import Value, Process
from ctypes import c_bool
from pyartnet import ArtNetNode, DmxChannel

import pyaudio
import numpy as np
import aubio
import time
import asyncio

class ArtNetBeatProcess:

    def __init__(self, beat_callback):
        self.process = Process(target=self._run_async)
        self.request_exit = Value(c_bool, False)
        self.beat_callback = beat_callback
        self.last_beat_at = time.time_ns()
        self.bpm_avg = 0

    def cb(ch: DmxChannel):
        print("dmx" + ch.get_channel_values())


    async def __run(self):
        print("Beat Detector Start")

        node = ArtNetNode(host="192.168.0.80", port=6454, broadcast=True)
        await node.start()
        universe = node.add_universe(0)

        channel = universe.add_channel(start=7, width=8)

        channel.callback_value_changed = self.cb

        while not self.request_exit.value:
            time.sleep(1)

        print("Beat Detector Stop")


    def _run_async(self):
        asyncio.run(self.__run())


    def start(self):
        self.process.start()


    def stop(self):
        print("Beat Detector request stop")
        self.request_exit.value = True
        self.process.join()
