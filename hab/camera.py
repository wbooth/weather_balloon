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

        # camera warm up (per manual)
        time.sleep(2)

    def __del__(self):
        self.close()

    def get_file_name(self, video=False):
        """
        return a file name with a time stamp 
        :return: file name
        """

        file_format = 'jpg'
        if video:
            file_format = 'h264'

        return os.path.join(self.base_dir, 'hab_{time}.{file_format}'.format(time=int(time.time()), file_format=file_format))

    def record_picture(self):
        self.capture(self.get_file_name(video=False))

    def record_video(self, record_time=60):
        self.start_recording(self.get_file_name(video=True))
        self.wait_recording(record_time)
        self.stop_recording()

    def record_session(self):
        print('record session')
        self.record_picture()
        self.record_video()
