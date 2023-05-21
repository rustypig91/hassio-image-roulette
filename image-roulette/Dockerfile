ARG BUILD_FROM
FROM $BUILD_FROM

# Install requirements for add-on
RUN apk add --no-cache python3 py3-pip
RUN pip3 install flask waitress

# Copy data for add-on
COPY run.sh /
COPY run.py /image-roulette/
COPY templates/index.html /image-roulette/templates/
RUN chmod a+x /run.sh

# CONFIG_PATH=/data/options.json
# TARGET="$(bashio::config 'target')"

CMD [ "./run.sh" ]