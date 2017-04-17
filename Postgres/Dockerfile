FROM postgres

VOLUME data:/var/lib/postgresql
ADD create-tables.sql /docker-entrypoint-initdb.d/
RUN apt-get update