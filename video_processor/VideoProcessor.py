import cv2
from apscheduler.schedulers.background import BackgroundScheduler
from deepface import DeepFace
from .settings import INTERVAL


class VideoProcessor:
    def __init__(self):
        self.cam = cv2.VideoCapture(0)
        self.sched = BackgroundScheduler()
        self.image = None
        self.data = None

    def start_sheduler(self):
        self.sched.add_job(self.process_input, 'interval', seconds=INTERVAL)
        self.sched.start()
        # self.sched.add_job(self.process_input, 'interval', seconds=1)

    def process_input(self):
        success, frame = self.cam.read()
        if not success:
            raise Exception("Failed to read from camera")
        # Get coordinates of faces from the image
        try:
            self.data = DeepFace.analyze(frame, actions=['emotion'])
        except ValueError:
            self.data = None

    def __del__(self):
        self.cam.release()
