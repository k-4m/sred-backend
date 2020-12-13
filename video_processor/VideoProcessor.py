import cv2
from apscheduler.schedulers.blocking import BlockingScheduler
from fer import FER


class VideoProcessor:
    def __init__(self):
        self.cam = cv2.VideoCapture(0)
        self.sched = BlockingScheduler()
        self.detector = FER()
        self.image = ""
        self.data = ""

    def start_sheduler(self):
        self.sched.add_job(self.process_input, 'interval', seconds=5)
        self.sched.start()
        # self.sched.add_job(self.process_input, 'interval', seconds=1)

    def process_input(self):
        print("here")
        success, frame = self.cam.read()
        if not success:
            raise Exception("Failed to read from camera")
        self.image = frame
        print(self.detector.detect_emotions(frame))


    def __del__(self):
        self.cam.release()
