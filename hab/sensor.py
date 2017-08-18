import os
import logging
from sense_hat import SenseHat
from . import utility


class Sensor(SenseHat):
    def __init__(self, base_dir):
        SenseHat.__init__(self)
        
        self.set_screen_color('red')
        
        self.base_dir = base_dir
        self.pressure_at_start = 1000  # standard millibars at sea level
        self.create_data_file()
        
        self.data_points = {
            'altitude': self.get_altitude,
            'temp_h': self.get_temperature_from_humidity,
            'temp_p': self.get_temperature_from_pressure,
            'humidity': self.get_humidity,
            'pressure': self.get_pressure,
            'orientation_pitch': self.get_orientation_pitch,
            'orientation_roll': self.get_orientation_roll,
            'orientation_yaw': self.get_orientation_yaw,
        }

    def __del__(self):
        self.clear()

    def set_screen_color(self, color):

        rgb = {
            'red': [255, 0, 0],
            'yellow': [255, 255, 0],
            'green': [0, 255, 0]
        }

        try:
            self.set_pixels([rgb[color.lower()] for _ in range(64)])
        except KeyError:
            logging.error('color not recognized, add rgb conversion')

    def get_data_file_name(self):
        return os.path.join(self.base_dir, 'hab_data.csv')
    
    def create_data_file(self):
        utility.Util.write_csv(filename=self.get_data_file_name(),
                               data=['timestamp', 'type', 'value'])
        
    def ready(self):
        self.set_screen_color(color='yellow')

    def start(self):
        self.pressure_at_start = self.get_pressure()
        self.set_screen_color(color='green')

    def get_altitude(self):
        # convert pressure in millibars to (approx.) altitude in feet.
        # to convert to meters, 0.3048 * altitude
        return (1 - (self.get_pressure() / 1013.25) ** 0.190284) * 145366.45
    
    def get_orientation_pitch(self):
        return self.get_orientation()['pitch']
    
    def get_orientation_roll(self):
        return self.get_orientation()['roll']
    
    def get_orientation_yaw(self):
        return self.get_orientation()['yaw']
    
    def log_data(self):
            for data_type, get_value in self.data_points.items():
                msg = "{name}: {value}".format(name=data_type, value=get_value())
                logging.debug(msg)
                utility.Util.write_csv(filename=self.get_data_file_name(),
                                       data=[utility.Util.get_timestamp(), data_type, get_value()])
