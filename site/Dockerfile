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

# Base settings
ENV SITE_ROOT /root/site
ENV BIN_DIR ${SITE_ROOT}/bin
ENV VAR_DIR /root/var
ENV TMP_DIR /root/tmp
ENV SHARE_DIR /root/shared

# File generation destinations
ENV UI_NODE_MODULES_DIR ${TMP_DIR}/npm/ui/node_modules
ENV TEST_NODE_MODULES_DIR ${TMP_DIR}/npm/test/node_modules
ENV MIGRATION_MODULE_DIR ${VAR_DIR}
ENV WEBPACK_OUTPUT_DIR ${VAR_DIR}/static

# Config file locations
ENV WEBPACK_CONF_PATH ${SITE_ROOT}/src/web
ENV UI_NPM_JSON_PATH ${SITE_ROOT}/src/web
ENV TEST_NPM_JSON_PATH ${SITE_ROOT}/tests/ui

# environment variables required by other softwares
ENV NODE_PATH ${UI_NODE_MODULES_DIR}:${NODE_PATH}
ENV NODE_PATH ${TEST_NODE_MODULES_DIR}:${NODE_PATH}
ENV PYTHONPATH ${MIGRATION_MODULE_DIR}:${SITE_ROOT}:${PYTHONPATH}
ENV PATH ${UI_NODE_MODULES_DIR}/.bin:${PATH}
ENV PATH ${TEST_NODE_MODULES_DIR}/.bin:${PATH}
ENV PATH ${BIN_DIR}:${PATH}

RUN mkdir -p ${VAR_DIR}
RUN mkdir -p ${TMP_DIR}
RUN mkdir -p ${SHARE_DIR}
RUN mkdir -p ${SITE_ROOT}

# install source
COPY . ${SITE_ROOT}
RUN chmod gu+x -R ${BIN_DIR}
RUN pipref
RUN yarnref --ci
RUN webpackref
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
RUN cp ${SITE_ROOT}/supervisord.conf /etc/supervisor/conf.d/supervisord.conf
CMD supervisord -n -c /etc/supervisor/conf.d/supervisord.conf
