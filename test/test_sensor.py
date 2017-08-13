from unittest import TestCase
from hab import sensor

class TestSensor(TestCase):
    def __init__(self):
        self.sensor = sensor.Sensor()

    def test_set_screen_color(self):
        self.assertRaises(KeyError, self.sensor.set_screen_color('xxx'))

    def test_ready(self):
        self.fail()

    def test_start(self):
        self.fail()

    def test_create_logfile(self):
        self.fail()

    def test_log_data(self):
        self.fail()
