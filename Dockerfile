FROM python:3
ENV PYTHONUNBUFFERED 1
RUN mkdir /codedock
WORKDIR /code
ADD requirements.txt /code/
RUN pip install -r requirements.txt
ADD . /code/