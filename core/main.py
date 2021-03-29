import math
from time import sleep
from Helios import Helios
import random
from LaserThread import LaserThread


laser = LaserThread()

laser.start()

laser.sweep()

sleep(2)

laser.stop()
