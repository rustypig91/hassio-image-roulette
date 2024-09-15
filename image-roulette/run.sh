#!/usr/bin/with-contenv bashio

IMAGES_PATH=$(bashio::config 'images_directory')
export IMAGES_PATH
PERIOD_SECONDS=$(bashio::config 'period_seconds')
export PERIOD_SECONDS
CUSTOM_HTML=$(bashio::config 'custom_html')
export CUSTOM_HTML

. /image-roulette/venv/bin/activate
cd /image-roulette
python3 run.py