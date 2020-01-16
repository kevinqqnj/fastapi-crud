# pull official base image
FROM python:3.8.1-alpine

# set work directory
WORKDIR /usr/src

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# copy requirements file
COPY ./requirements.txt /usr/src/requirements.txt

# install dependencies/ --no-cache / 
RUN set -eux \
    && apk add --virtual .build-deps build-base \
        libressl-dev libffi-dev gcc musl-dev python3-dev \
    && pip install --upgrade pip setuptools wheel \
    && pip install -r /usr/src/requirements.txt 
    # && rm -rf /root/.cache/pip

# copy project
COPY . /usr/src/
