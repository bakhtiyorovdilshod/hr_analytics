# pull official base image
FROM python:3.11.2-slim-buster

# set working directory
RUN mkdir -p /web/
ENV APP_HOME=/web/lazy_work
WORKDIR ${APP_HOME}

RUN mkdir ${APP_HOME}/staticfiles
RUN mkdir ${APP_HOME}/media


# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install system dependencies
RUN apt-get update \
  && apt-get -y install netcat gcc \
  && apt-get clean \


# install python dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt ${APP_HOME}/requirements.txt
RUN pip install -r requirements.txt


# add app
COPY . ${APP_HOME}
