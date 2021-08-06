import ctypes

# #Load and initialize library
# HeliosLib = ctypes.cdll.LoadLibrary("./libHeliosDacAPI.so")
# numDevices = HeliosLib.OpenDevices()
# print("Found ", numDevices, "Helios DACs")

# #Create sample frames
# frames = [0 for x in range(30)]
# frameType = HeliosPoint * 1000
# x = 0
# y = 0
# for i in range(30):
#     y = round(i * 0xFFF / 30)
#     frames[i] = frameType()
#     for j in range(1000):
#         if (j < 500):
#             x = round(j * 0xFFF / 500)
#         else:
#             x = round(0xFFF - ((j - 500) * 0xFFF / 500))

#         frames[i][j] = HeliosPoint(int(x),int(y),255,255,255,255)

# #Play frames on DAC
# for i in range(150):
#     for j in range(numDevices):
#         statusAttempts = 0
#         # Make 512 attempts for DAC status to be ready. After that, just give up and try to write the frame anyway
#         while (statusAttempts < 512 and HeliosLib.GetStatus(j) != 1):
#             statusAttempts += 1
#         HeliosLib.WriteFrame(j, 30000, 0, ctypes.pointer(frames[i % 30]), 1000) #Send the frame


# HeliosLib.CloseDevices()

class HeliosPoint(ctypes.Structure):
    #_pack_=1
    _fields_ = [('x', ctypes.c_uint16),
        ('y', ctypes.c_uint16),
        ('r', ctypes.c_uint8),
        ('g', ctypes.c_uint8),
        ('b', ctypes.c_uint8),
        ('i', ctypes.c_uint8)]

    def str(self):
        return f"<HeliosPoint x: {self.x}, x: {self.y}, r: {self.r}, g: {self.g}, b: {self.b}>"

class Helios:

   
    def __init__(self):
        self.max_brighteness = 1
        self.helios_lib = ctypes.cdll.LoadLibrary("/home/pi/laser_pi/lib/libHeliosDacAPI.so")

    def open(self):
        self.num_devices = self.helios_lib.OpenDevices()
        print("Found ", self.num_devices, "Helios DACs")

    def send_frame(self, frame):
        num_points = len(frame)
        frame_type = HeliosPoint * num_points
        helios_frame = frame_type()

        for i in range(num_points):
            helios_frame[i] = self.__map_point(frame[i])

        self.helios_lib.WriteFrame(0, 15000, 0, ctypes.pointer(helios_frame), num_points)

    def close(self):
        self.helios_lib.CloseDevices()


    def __map_point(self, point):
        x = (int) (point['x'] * 4096 * 0.5 + 1000)
        y = (int) (point['y'] * 4096 * 0.5 + 1900)
        r = (int) (point['r'] * self.max_brighteness * 255.0)
        g = (int) (point['g'] * self.max_brighteness * 255.0)
        b = (int) (point['b'] * self.max_brighteness  * 255.0) 
        
        return HeliosPoint(x, y, r, g, b, 50)
