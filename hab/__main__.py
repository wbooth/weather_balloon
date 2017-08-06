import argparse
from . import app


def main():
    parser = argparse.ArgumentParser(description='High Altitude Weather Balloon')

    parser.add_argument('--dir', default='/tmp', help='Base directory for logs, images, and data')
    parser.add_argument('--sensor', default=1, help='Use Sensor')
    parser.add_argument('--camera', default=1, help='Use Camera')

    args = parser.parse_args()

    application = app.App(args)
    application.execute()

if __name__ == '__main__':
    main()
