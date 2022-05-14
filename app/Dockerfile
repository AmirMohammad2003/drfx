FROM python:3.10-alpine

LABEL Author="AmirMohammad"

ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt requirements.txt

RUN apk add --update --no-cache postgresql-client
RUN apk add --update --no-cache --virtual .temp-build-deps \
    gcc build-base linux-headers libffi-dev libc-dev postgresql-dev
RUN pip install -r requirements.txt
RUN apk del .temp-build-deps

RUN mkdir /app
WORKDIR /app
COPY . /app

RUN adduser -D django
RUN chown -R django:django /app

USER django
