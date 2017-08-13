import os
from sense_hat import SenseHat
from . import utility


class Sensor(SenseHat):
    def __init__(self):
        SenseHat.__init__(self)
        self.set_screen_color('red')

        self.pressure_at_start = 1000  # average millibars at sea level
        
        self.data_points = {
            'temp_h': self.get_temperature_from_humidity,
            'temp_p': self.get_temperature_from_pressure,
            'humidity': self.get_humidity,
            'pressure': self.get_pressure,
            'orientation': self.get_orientation,  # dict of x, y, z = pitch, roll, yaw
            'mag': self.get_compass_raw,          # dict of x, y, z = pitch, roll, yaw
            'accel': self.get_accelerometer_raw,  # dict of x, y, z = pitch, roll, yaw
            'gyro': self.get_gyroscope_raw,       # dict of x, y, z = pitch, roll, yaw
        }

    def __del__(self):
        self.clear()

    def set_screen_color(self, color=None):
        """
        set all pixels a single rgb color
        :param color: [r, g, b]
        :return:
        """

        if not color:
            self.clear()
            return

        rgb = {
            'red': [255, 0, 0],
            'yellow': [255, 255, 0],
            'green': [0, 255, 0]
        }

        try:
            self.set_pixels([rgb[color.to_lower()] for _ in range(64)])
        except KeyError:
            print('color not recognized, add rgb conversion')

    def ready(self):
        self.set_screen_color(color='yellow')

    def start(self):
        self.pressure_at_start = self.get_pressure()
        self.set_screen_color(color='green')

    def create_logfile(self, base_dir):
        """
        Create log file
        :return: 
        """
        
        header = ["temp_h" ,"temp_p", "humidity", "pressure", "pitch", "roll", "yaw", "mag_x", "mag_y", "mag_z",
                  "accel_x", "accel_y", "accel_z", "gyro_x", "gyro_y", "gyro_z", "timestamp"]

    def get_altitude(self):
        """
        convert pressure in millibars to (approx.) altitude in feet.
        :return:
        """

        altitude_in_feet = (1 - (self.get_pressure() / 1013.25) ** 0.190284) * 145366.45

        # to meters = 0.3048 * altitude_in_meters

        return altitude_in_feet

    def log_data(self):
        print('logging...')
        for data_point in self.data_points:
            print(data_point())
        print('got em')
