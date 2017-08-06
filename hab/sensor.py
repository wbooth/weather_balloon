from sense_hat import SenseHat
import os

class Sensor(SenseHat):
    def __init__(self):
        # light up
        self.start()

    def __del__(self):
        self.clear()

    def ready(self):
        # set screen to red
        self.set_pixels([[255, 0, 0] for _ in range(64)])  # red
        
        # create logfile
        self.create_logfile()
        
        # create photo directory
        self.create_photo_directory()
        
        # create video directory
        self.create_video_directory()
                
        # set screen to yellow
        self.set_pixels([[255, 255, 0] for _ in range(64)])  # yellow
        # self.set_pixels([[0, 255, 0] for _ in range(64)])  # green

    def create_logfile(self):
        header = ["temp_h","temp_p","humidity","pressure","pitch","roll","yaw", "mag_x","mag_y","mag_z", 
                  "accel_x","accel_y","accel_z", "gyro_x","gyro_y","gyro_z", "timestamp"]
        
        
        
    def create_photo_directory(self):
        pass

    def create_video_directory(self):
        pass

