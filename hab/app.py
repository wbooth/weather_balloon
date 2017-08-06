from . import sensor
from . import camera


class App:
    def __init__(self, args):
        # check and store available size on startup
        self.camera = camera.Camera()
        self.sensor = sensor.Sensor()
        print(args)
        pass

    def __del__(self):
        pass

    def execute(self):
        self.sensor.ready()
