#!/usr/bin/with-contenv bashio

IMAGES_PATH=$(bashio::config 'images_directory')
export IMAGES_PATH
PERIOD_SECONDS=$(bashio::config 'period_seconds')
export PERIOD_SECONDS
TEMPLATES_FOLDER=$(bashio::config 'templates_folder')
export TEMPLATES_FOLDER

. /image-roulette/venv/bin/activate
cd /image-roulette
python3 run.py