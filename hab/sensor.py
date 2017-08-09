import os
from sense_hat import SenseHat


class Sensor(SenseHat):
    def __init__(self):
        SenseHat.__init__(self)

        # set screen to red
        self.set_pixels([[255, 0, 0] for _ in range(64)])  # red

    def __del__(self):
        self.clear()

    def ready(self):
        # set screen to yellow
        self.set_pixels([[255, 255, 0] for _ in range(64)])  # yellow

    def start(self):
        # set screen to green
        self.set_pixels([[0, 255, 0] for _ in range(64)])  # green

    def create_logfile(self, base_dir):
        """
        Create log file
        :return: 
        """
        
        header = ["temp_h" ,"temp_p", "humidity", "pressure", "pitch", "roll", "yaw", "mag_x", "mag_y", "mag_z",
                  "accel_x", "accel_y", "accel_z", "gyro_x", "gyro_y", "gyro_z", "timestamp"]

    def log_data(self):
        print('logging...')
        sense_data = {}
        sense_data['temp_h'] = self.get_temperature_from_humidity()
        print(sense_data)
