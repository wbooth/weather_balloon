import os
import time
from picamera import PiCamera
from . import utility


class Camera(PiCamera):
    def __init__(self, base_dir='/tmp'):
        PiCamera.__init__(self)

        self.base_dir = base_dir

        self.resolution = (1024, 768)
        self.start_preview()
        self.camera_warmup()

    def __del__(self):
        self.close()

    @staticmethod
    def camera_warmup():
        time.sleep(2)

    def get_file_name(self, format):
        return os.path.join(self.base_dir, 'hab_{time}.{format}'.format(time=utility.Util.get_timestamp(),
                                                                        format=format))

    def record_picture(self):
        self.capture(self.get_file_name(format='jpg'))

    def record_video(self, record_time=60):
        self.start_recording(self.get_file_name(format='h264'))
        self.wait_recording(record_time)
        self.stop_recording()

    def record_session(self):
        self.record_picture()
        self.record_video()
