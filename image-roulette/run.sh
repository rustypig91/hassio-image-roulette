#!/usr/bin/with-contenv bashio

IMAGES_PATH=$(bashio::config 'images_directory')
export IMAGES_PATH

cd /image-roulette
python3 run.py