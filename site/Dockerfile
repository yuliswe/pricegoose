FROM ubuntu:18.04

ENV LC_ALL C.UTF-8
ENV LANG C.UTF-8
ENV LANGUAGE C.UTF-8
ENV DEBIAN_FRONTEND noninteractive

RUN apt-get update --fix-missing
RUN apt-get -y install python3.8 python3-pip
RUN apt-get -y install libpq-dev postgresql postgresql-contrib
RUN apt-get -y install wait-for-it
RUN apt-get -y install libnss3 chromium-browser
RUN ln -s /usr/bin/chromium-browser /usr/bin/chrome

# install nodejs
RUN apt-get -y install curl
RUN curl -sL https://deb.nodesource.com/setup_13.x | bash -
RUN apt-get -y install supervisor
# install yarn
RUN curl -sS https://dl.yarnpkg.com/debian/pubkey.gpg | apt-key add -
RUN echo "deb https://dl.yarnpkg.com/debian/ stable main" | tee /etc/apt/sources.list.d/yarn.list
RUN apt-get update
RUN apt-get -y install yarn

ENV SITE_ROOT /root/site

ENV BIN_DIR ${SITE_ROOT}/bin
ENV VAR_DIR /root/var
ENV SHARED_DIR /root/shared
ENV UI_NODE_PATH ${VAR_DIR}/ui_node_modules
ENV TEST_NODE_PATH ${VAR_DIR}/test_node_modules
ENV NODE_PATH ${UI_NODE_PATH}:${TEST_NODE_PATH}:${NODE_PATH}

RUN mkdir -p ${VAR_DIR}
RUN mkdir -p ${SHARED_DIR}

ENV WEBPACK_CONF_DIR ${SITE_ROOT}/src/web
ENV DJANGO_MANAGE_PY_PATH ${SITE_ROOT}/manage.py
ENV NPM_PACKAGES_JSON_DIR ${SITE_ROOT}/src/web
ENV TEST_NPM_PACKAGES_JSON_DIR ${SITE_ROOT}/tests/ui

ENV PYTHONPATH ${VAR_DIR}:${SITE_ROOT}:${PYTHONPATH}
ENV PATH ${UI_NODE_PATH}/.bin:${PATH}
ENV PATH ${TEST_NODE_PATH}/.bin:${PATH}
ENV PATH ${BIN_DIR}:${PATH}

# install source
COPY . ${SITE_ROOT}
RUN chmod g+x -R ${BIN_DIR}
RUN pipref && yarnref
# set up database
WORKDIR ${SITE_ROOT}
RUN runscript make-migration-dirs
RUN service postgresql start && \
    wait-for-it localhost:5432 && \
    su - postgres -c "psql -c \"ALTER USER postgres PASSWORD 'postgres';\"" && \
    su - postgres -c "psql -c \"CREATE DATABASE site;\"" && \
    manage makemigrations && \
    manage migrate

WORKDIR ${SITE_ROOT}
# set up supervisord
COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf
CMD supervisord -n -c /etc/supervisor/conf.d/supervisord.conf
