FROM python:3.6.8-alpine3.10
# init
RUN apk update
RUN apk upgrade
RUN apk add bash
RUN rm /bin/sh && ln -s /bin/bash /bin/sh
RUN mkdir /www
WORKDIR /www
COPY requirements.txt /www/
# setup
RUN apk --no-cache add \
    postgresql-client \
    postgresql-dev \
    build-base \
    gettext \
    curl \
    openssh \
    libffi-dev
RUN pip3 install --upgrade pip
RUN pip3 install -r requirements.txt
# clean
RUN apk del -r python3-dev postgresql
# prep
ENV PYTHONUNBUFFERED 1
COPY . /www/
ADD ./.profile.d /app/.profile.d
RUN chmod u+x manage.py
