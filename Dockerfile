# FROM python:3.6
#ENV PYTHONUNBUFFERED 1
#RUN mkdir /config
#ADD ./requirements.txt /config/
#RUN pip install -r /config/requirements.txt
#RUN mkdir /src;
#EXPOSE 8000
#WORKDIR /src
#COPY . /src/
# Run the app.  CMD is required to run on Heroku
# $PORT is set by Heroku
#CMD python manage.py makemigrations && python manage.py collectstatic --no-input && python manage.py migrate

FROM alpine
# init
RUN mkdir /www
WORKDIR /www
COPY requirements.txt /www/
# setup
RUN apk update
RUN apk upgrade
RUN apk --no-cache add \
    python3 \
    python3-dev \
    postgresql-client \
    postgresql-dev \
    build-base \
    gettext
RUN pip3 install --upgrade pip
RUN pip3 install -r requirements.txt
# clean
RUN apk del -r python3-dev postgresql
# prep
ENV PYTHONUNBUFFERED 1
COPY . /www/