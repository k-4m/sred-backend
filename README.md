# sred-backend

### setting up

This project is running on Python 3.6. 
Create a virtualenv and then install dependencies:
```
pip install -v requirements.txt
```

### usage
Program will require access to your web camera in order to run.
When requested permissions are given, you will be able to get json output on the `localhost:3000`.
(Host and port can be updated in `video_processor/settings.py`):

```
{
  "image": "/9j/4AAQSkZJRgAB...6Em5RP/9k=",
  "emotions_data": {
    "emotion": {
      "angry": 1.9495684653520584,
      "disgust": 4.85497508861954e-7,
      "fear": 0.5955945234745741,
      "happy": 3.42639427941549e-7,
      "sad": 39.424800872802734,
      "surprise": 0.0003347103756823344,
      "neutral": 58.029705286026
    },
    "dominant_emotion": "neutral"
  }
}
``` 

In case nothing is rendered yet or there are no faces found, following message will be returned:
```
{
  "error": "no faces found"
}
```