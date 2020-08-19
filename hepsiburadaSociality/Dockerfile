FROM python:3

ENV PYTHONUNBUFFERED 1

WORKDIR /backend

ADD . /backend

COPY ./requirements.txt  /backend/requirements.txt

RUN pip install -r requirements.txt

COPY . /backend

EXPOSE 8000