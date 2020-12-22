import cv2
import face_recognition
from PIL import Image, ImageDraw, ImageChops
import base64
from io import BytesIO
from apscheduler.schedulers.background import BackgroundScheduler
from deepface import DeepFace
from .settings import INTERVAL

color_of_emotion = {
    "angry": "#F06543",
    "disgust": "#4E937A",
    "fear": "#284B63",
    "happy": "#FFE347",
    "sad": "#A195EE",
    "surprise": "#0072BB",
    "neutral": "#BBC7A4"
}

class VideoProcessor:
    def __init__(self):
        self.cam = cv2.VideoCapture(0)
        self.sched = BackgroundScheduler()
        self.image = None
        self.data = None

    def start_sheduler(self):
        self.sched.add_job(self.process_input, 'interval', seconds=INTERVAL)
        self.sched.start()

    @staticmethod
    def image_with_outlined_face(frame, outline_color="green"):
        face_locations = face_recognition.face_locations(frame)
        image = Image.fromarray(frame)
        r, g, b = image.split()
        image = Image.merge('RGB', (b, g, r))
        draw = ImageDraw.Draw(image)
        for top, left, bottom, right in face_locations:
            draw.rectangle([left, top, right, bottom], outline=outline_color, width=10)
        buffered = BytesIO()
        image.save(buffered, format="JPEG")
        return base64.b64encode(buffered.getvalue())

    def process_input(self):
        success, frame = self.cam.read()
        if not success:
            raise Exception("Failed to read from camera")
        # Get coordinates of faces from the image
        try:
            self.data = DeepFace.analyze(frame, actions=['emotion'])
            self.image = self.image_with_outlined_face(
                frame,
                outline_color=color_of_emotion[self.data["dominant_emotion"]]
            )

        except ValueError:
            self.data = None

    def __del__(self):
        self.cam.release()
