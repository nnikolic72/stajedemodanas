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

FROM python:3.6.6-alpine3.8
# init
RUN apk update
RUN apk upgrade
RUN apk add bash
ADD sh-wrapper.sh /bin/sh-wrapper.sh
RUN chmod a+x /bin/sh-wrapper.sh
RUN rm /bin/sh && ln -s /bin/sh-wrapper.sh /bin/sh
RUN mkdir /www
WORKDIR /www
COPY requirements.txt /www/
# setup
RUN apk --no-cache add \
    python3 \
    python3-dev \
    postgresql-client \
    postgresql-dev \
    build-base \
    gettext \
    curl \
    openssh
RUN pip3 install --upgrade pip
RUN pip3 install -r requirements.txt
# clean
RUN apk del -r python3-dev postgresql
# prep
ENV PYTHONUNBUFFERED 1
COPY . /www/
ADD ./.profile.d /app/.profile.d
# RUN ./manage.py collectstatic --no-input
# RUN ./manage.py migrate
