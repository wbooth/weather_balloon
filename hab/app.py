import os
import time
import threading
from . import sensor
from . import camera
from . import utility


class App:
    def __init__(self, args):
        self.threads = []
        print(args)

        # create directory for data and recordings
        utility.Util.create_dir(args.dir)

        # check and store available size on startup
        self.sensor = sensor.Sensor()
        self.sensor.low_light = True
        self.camera = camera.Camera(base_dir=args.dir)

        self.sensor.ready()

    def __del__(self):
        pass

    def get_stick_pressed(self):
        """
        Returns True if stick is pressed otherwise False
        :return: Stick is pressed
        """

        for event in self.sensor.stick.get_events():
            if event.action == 'pressed':
                return True

        return False

    @staticmethod
    def interval_task(task, interval_time=-1):
        # update pass args
        while True:
            task()
            if interval_time:
                time.sleep(interval_time)

    def thread_monitor(self):
        print('monitoring...')

    def execute(self):
        print('executing...')

        # wait for input from joy stick to continue
        # while True:
        #     if self.get_stick_pressed():
        #         self.sensor.start()
        #         break

        try:
            monitor_thread = threading.Thread(target=self.interval_task, args=(self.thread_monitor, 0,))
            self.threads.append(monitor_thread)
            monitor_thread.start()

            camera_thread = threading.Thread(target=self.interval_task, args=(self.camera.record_session, 0,))
            self.threads.append(camera_thread)
            camera_thread.start()

            sensor_thread = threading.Thread(target=self.interval_task, args=(self.sensor.log_data, 0,))
            self.threads.append(sensor_thread)
            sensor_thread.start()
        except:
            print('could not start threads')
