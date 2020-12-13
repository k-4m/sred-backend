import sys
import os
from video_processor import VideoProcessor


if __name__ == '__main__':
    try:
        video_processor = VideoProcessor()
        video_processor.start_sheduler()
        while True:
            continue
    except KeyboardInterrupt:
        print('Exiting...')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)

