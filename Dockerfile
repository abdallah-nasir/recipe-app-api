FROM python:3.10.13-alpine
LABEL maintainer="abdallah nasir"

ENV PYTHONUNBUFFERED 1
COPY ./requirements.txt /tmp/requirements.txt
COPY ./app /app