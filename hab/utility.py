import os
import csv
import time
import logging


class Util:
    
    @staticmethod
    def get_timestamp():
        return int(time.time())
    
    @staticmethod
    def write_csv(filename, data):
        with open(filename, 'a') as file:
            writer = csv.writer(file)
            writer.writerow(data)

    @staticmethod
    def create_dir(directory):
        if not os.path.exists(directory):
            logging.debug('creating directory {directory}'.format(directory=directory))
            os.makedirs(directory)
