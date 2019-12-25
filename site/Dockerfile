FROM ubuntu:latest

ENV LC_ALL C.UTF-8
ENV LANG C.UTF-8
ENV LANGUAGE C.UTF-8
ENV DEBIAN_FRONTEND noninteractive

RUN apt-get update --fix-missing
RUN apt-get -y install python3.7 python3.7-dev python3-pip
RUN apt-get -y install libpq-dev postgresql postgresql-contrib
RUN apt-get -y install wait-for-it
RUN apt-get -y install libnss3 chromium-browser
RUN ln -s /usr/bin/chromium-browser /usr/bin/chrome

# install nodejs
RUN apt-get -y install curl
RUN curl -sL https://deb.nodesource.com/setup_10.x | bash -
RUN apt-get -y install nodejs
RUN apt-get -y install supervisor
# install yarn
RUN curl -sS https://dl.yarnpkg.com/debian/pubkey.gpg | apt-key add -
RUN echo "deb https://dl.yarnpkg.com/debian/ stable main" | tee /etc/apt/sources.list.d/yarn.list
RUN apt-get update
RUN apt-get -y install yarn

# set environment
ENV SITE_ROOT /root/site
ENV NODE_PATH /root/var/node_modules
ENV PATH /root/bin:${PATH}
ENV PATH ${NODE_PATH}/.bin:${PATH}
RUN mkdir /root/shared
RUN mkdir /root/var

WORKDIR /root/var
COPY requirements.txt .
RUN python3.7 -m pip install -r requirements.txt
COPY package.json .
COPY yarn.lock .
RUN yarn install --dev --modules-folder ${NODE_PATH}
# copy source
COPY bin /root/bin
RUN chmod u+x /root/bin/*
COPY . /root/site
WORKDIR /root/site
# set up database
ENV PYTHONPATH /root
RUN python3.7 manage.py runscript make-migration-dirs
RUN service postgresql start && \
    wait-for-it localhost:5432 && \
    su - postgres -c "psql -c \"ALTER USER postgres PASSWORD 'postgres';\"" && \
    su - postgres -c "psql -c \"CREATE DATABASE droppie;\"" && \
    python3.7 manage.py makemigrations && \
    python3.7 manage.py migrate

# set up supervisord
COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf
CMD supervisord -n -c /etc/supervisor/conf.d/supervisord.conf
