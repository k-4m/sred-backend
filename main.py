import sys
import os
import json
from flask import Flask
from flask_restful import Resource, Api, reqparse
from flask_cors import CORS
from video_processor import VideoProcessor, API_HOST, API_PORT

app = Flask(__name__)
CORS(app)
api = Api(app)

video_processor = VideoProcessor()


class EmotionsDetection(Resource):
    def get(self):
        return app.response_class(
            response=json.dumps(video_processor.data),
            status=200,
            mimetype='application/json'
        )


api.add_resource(EmotionsDetection, '/', methods=['GET'])

if __name__ == '__main__':
    try:
        video_processor.start_sheduler()
        app.run(host=API_HOST, port=API_PORT)
    except KeyboardInterrupt:
        print('Exiting...')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)
