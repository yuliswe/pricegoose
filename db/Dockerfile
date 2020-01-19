FROM ubuntu:latest

ENV LC_ALL C.UTF-8
ENV LANG C.UTF-8
ENV LANGUAGE C.UTF-8
ENV DEBIAN_FRONTEND noninteractive

RUN apt-get update --fix-missing
RUN apt-get install -y libpq-dev postgresql postgresql-contrib
RUN apt-get install -y wait-for-it

COPY ./postgresql.conf /etc/postgresql/10/main/postgresql.conf
COPY ./pg_hba.conf /etc/postgresql/10/main/pg_hba.conf

RUN service postgresql start && \
    wait-for-it localhost:5432 && \
    su - postgres -c "psql -c \"ALTER USER postgres PASSWORD 'postgres';\"" && \
    su - postgres -c "psql -c \"CREATE DATABASE site;\""

CMD service postgresql start && sleep inf
