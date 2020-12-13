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
  "emotion": {
    "angry": 0.011994630040135235,
    "disgust": 2.153855739595034e-9,
    "fear": 0.004935113247483969,
    "happy": 1.9427111030978494e-7,
    "sad": 0.9675447829067707,
    "surprise": 0.000003176235097157587,
    "neutral": 99.01552200317383
  },
  "dominant_emotion": "neutral"
}
``` 

In case nothing is rendered yet or there are no faces found, following message will be returned:
```
{
  "error": "no faces found"
}
```