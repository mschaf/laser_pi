import math

class Animation:

    def __init__(self, frame_callback, beat_event):
        self.frame_callback = frame_callback
        self.beat_event = beat_event

    def line_frame(self, x1, y1, x2, y2, num_points, r, g, b):
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
            frame.append({'x': x, 'y': y, 'r': r, 'g': g, 'b': b})

        frame[0]['r'] = 0
        frame[0]['g'] = 0
        frame[0]['b'] = 0

        frame[n - 1]['r'] = 0
        frame[n - 1]['g'] = 0
        frame[n - 1]['b'] = 0

        return frame

    def line_frame_single(self, x1, y1, x2, y2, num_points, r, g, b):
        n = num_points
        frame = []
        x_distance = max(x1, x2) - min(x1, x2)
        y_distance = max(y1, y2) - min(y1, y2)
        x_start = min(x1, x2)
        y_start = min(y1, y2)

        for i in range(n):
            p = (math.pi / n) / 2
            x = x_start + math.sin(p * i) * x_distance
            y = y_start + math.sin(p * i) * y_distance
            frame.append({'x': x, 'y': y, 'r': r, 'g': g, 'b': b})

        frame[0]['r'] = 0
        frame[0]['g'] = 0
        frame[0]['b'] = 0

        frame[n - 1]['r'] = 0
        frame[n - 1]['g'] = 0
        frame[n - 1]['b'] = 0

        return frame

    def line_points_a(self, s, e, num_points):
        return self.line_points(s[0], s[1], e[0], e[1], num_points)    


    def line_points(self, x1, y1, x2, y2, num_points):
        n = num_points
        points = []
        x_delta = x2 - x1
        y_delta = y2 - y1

        for i in range(n):
            p = math.pi / n
            x = x1 + x_delta / n * i
            y = y1 + y_delta / n * i
            points.append([x, y])

        return points


    def rotate(self, origin, point, angle):
        """
        Rotate a point counterclockwise by a given angle around a given origin.

        The angle should be given in radians.
        """
        ox, oy = origin
        px, py = point

        qx = ox + math.cos(angle) * (px - ox) - math.sin(angle) * (py - oy)
        qy = oy + math.sin(angle) * (px - ox) + math.cos(angle) * (py - oy)
        return qx, qy

    def circle_points(self, r,n=60, phase=0):
        return [(math.cos(2*math.pi/n*x + phase)*r,math.sin(2*math.pi/n*x + phase)*r) for x in range(0,n+1)]

