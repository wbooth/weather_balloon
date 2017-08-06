import os
import time
from picamera import PiCamera


class Camera(PiCamera):
    def __init__(self):
        self.base_dir = '/tmp'
        self.resolution = (1024, 768)
        self.start_preview()
    
        # create photo directory
        self.create_photo_directory()
    
        # create video directory
        self.create_video_directory()

    def get_file_name(self, movie=False):
        """
        return a file name with a time stamp 
        :return: file name
        """
        if movie:
            file_format = 'mp4'
        else:
            file_format = 'jpg'

        return os.path.join(self.base_dir, 'hab_{time}.{file_format}'.format(time=int(time.time()), file_format=file_format))

    def create_photo_directory(self):
        pass

    def create_video_directory(self):
        pass

    def record_picture(self):
        self.capture(self.get_file_name())

    def record_video(self):
        self.capture(self.get_file_name(movie=True))
