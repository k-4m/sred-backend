FROM python:3.6

EXPOSE 3000

COPY requirements.txt .

RUN pip install cmake

RUN pip install -r requirements.txt

RUN apt-get update

RUN apt-get install -y libgl1-mesa-glx

COPY ./src/ .

CMD [ "python3", "./main.py" ]