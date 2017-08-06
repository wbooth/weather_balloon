import os


class Util:

    def log(self, message):
        pass

    @staticmethod
    def create_dir(file_path):
        directory = os.path.dirname(file_path)
        if not os.path.exists(directory):
            os.makedirs(directory)
            
        return True
