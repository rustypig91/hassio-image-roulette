ARG BUILD_FROM
FROM $BUILD_FROM

# Install requirements for add-on
RUN apk add --no-cache python3 py3-pip
# Copy data for add-on
COPY run.sh /
COPY run.py /image-roulette/
COPY templates/index.html /image-roulette/templates/
RUN chmod a+x /run.sh

RUN python3 -m venv /image-roulette/venv
RUN . /image-roulette/venv/bin/activate && pip3 install flask waitress trafiklab-sl

# CONFIG_PATH=/data/options.json
# TARGET="$(bashio::config 'target')"

CMD [ "./run.sh" ]
