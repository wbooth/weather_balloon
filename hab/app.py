from . import sensor
from . import camera


class Application:
    def __init__(self, args):
        # check and store available size on startup
        self.camera = camera()
        self.sensor = sensor()
        print(args)
        pass

    def __del__(self):
        pass

    def execute(self):
        self.sensor.ready()
