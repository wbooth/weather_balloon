import os
import logging


class Util:
    def __init__(self):
        logging.basicConfig(filename='runtime.log',
                            filemode='w',
                            level=logging.DEBUG)

    def log(self, message):
        pass

    @staticmethod
    def create_dir(directory):
        # directory = os.path.dirname(file_path)
        if not os.path.exists(directory):
            print('creating directory {directory}'.format(directory=directory))
            os.makedirs(directory)
            
        return True
