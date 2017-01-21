FROM debian:jessie

# GENERAL DEPENDENCIES

RUN apt-get update && \
    apt-get -y install curl

# Pip
RUN apt-get -y install python-pip

# Gunicorn
RUN apt-get update
RUN pip install gunicorn

# Flask
RUN apt-get -y install python-dev
RUN pip install Flask

# Snowplow python tracker
RUN pip install snowplow-tracker

# Cron
RUN apt-get -y install cron
ADD docker/crontab /app/crontab
RUN crontab /app/crontab

# Project env and files
ENV PROJECT_HOME /Preco
RUN mkdir /Preco
RUN mkdir /Preco/src
RUN mkdir /Preco/data
COPY src /Preco/src/
COPY data /Preco/data/
COPY README.md /Preco/
RUN chmod u+x /Preco/src/main/script/autostart.sh

ENTRYPOINT ["/Preco/src/main/script/autostart.sh"]

# Build-time metadata as defined at http://label-schema.org
#ARG BUILD_DATE
#ARG VCS_REF
#ARG VERSION
#LABEL org.label-schema.build-date=$BUILD_DATE \
#      org.label-schema.name="snowplow-webhook" \
#      org.label-schema.description="Webhook based on pytghon tracker" \
#      org.label-schema.url="http://kolibero.eu" \
#      org.label-schema.vcs-ref=$VCS_REF \
#      org.label-schema.vcs-url="https://github.com/goliasz/snowplow-webhook" \
#      org.label-schema.vendor="KOLIBERO" \
#      org.label-schema.version=$VERSION \
#      org.label-schema.schema-version="1.0"
