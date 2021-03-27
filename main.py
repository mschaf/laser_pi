import math
from time import sleep
from Helios import Helios
import random

def hsv_to_rgb(h, s, v):
    if s == 0.0: v*=255; return (v, v, v)
    i = int(h*6.) # XXX assume int() truncates!
    f = (h*6.)-i; p,q,t = int(255*(v*(1.-s))), int(255*(v*(1.-s*f))), int(255*(v*(1.-s*(1.-f)))); v*=255; i%=6
    if i == 0: return (v, t, p)
    if i == 1: return (q, v, p)
    if i == 2: return (p, v, t)
    if i == 3: return (p, q, v)
    if i == 4: return (t, p, v)
    if i == 5: return (v, p, q)

helios = Helios()

frame = []

n = 100

def line_frame(x1, y1, x2, y2, num_points, r, g, b):
    n = num_points
    frame = []
    x_distance = max(x1, x2) - min(x1, x2)
    y_distance = max(y1, y2) - min(y1, y2)
    x_start = min(x1, x2)
    y_start = min(y1, y2)

    for i in range(n):
        p = math.pi / n
        x = x_start + math.sin(p * i) * x_distance
        y = y_start + math.sin(p * i) * y_distance
        frame.append( { 'x': x, 'y': y, 'r': r, 'g': g, 'b': b} )

    frame[0]['r'] = 0
    frame[0]['g'] = 0
    frame[0]['b'] = 0

    
    frame[n-1]['r'] = 0
    frame[n-1]['g'] = 0
    frame[n-1]['b'] = 0

    return frame

for i in range(n):
    x = math.cos(2 * math.pi / n * i) * 0.5 + 0.5
    y = math.sin(2 * math.pi / n * i) * 0.5 + 0.5

    point = { 'x': x, 'y': y, 'r': 1, 'g': 1, 'b': 1}
    frame.append(point)


helios.open()

try:
    rand = 0
    while True:
        rand += 1
        if rand == 4:
            rand = 0
        n = 200
        r,g,b = hsv_to_rgb(random.random(), 0.5, 1)
        num_points = 40
        

        for i in range(n):
            p = (1.0 / n) * i

            frame = None
            if rand == 2:
                frame = line_frame(p, 0, p, 1, num_points, r, g, b)
            if rand == 0:
                frame = line_frame(1-p, 0, 1-p, 1, num_points, r, g, b)
            if rand == 1:
                frame = line_frame(0, p, 1, p, num_points, r, g, b)
            if rand == 3:
                frame = line_frame(0, 1-p, 1, 1-p, num_points, r, g, b)
                    
            helios.send_frame(frame)

finally:
    helios.close()
