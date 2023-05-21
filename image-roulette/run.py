import os
import random
from flask import Flask, send_file, render_template

app = Flask(__name__)

IMAGES_PATH = os.getenv("IMAGES_PATH")

@app.route('/random')
def serve_random_picture():

    # Get a list of all the picture files in the folder
    picture_files = [file for file in os.listdir(IMAGES_PATH) if file.lower().endswith(('.jpg', '.jpeg', '.png'))]
    if len(picture_files) == 0:
        return f"No images found in image path ({IMAGES_PATH})"
    # Choose a random picture from the list
    random_picture = random.choice(picture_files)

    # Return the picture file
    return send_file(os.path.join(IMAGES_PATH, random_picture))

@app.route('/')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    from waitress import serve
    import logging
    logger = logging.getLogger("waitress")
    logger.setLevel(logging.INFO)
    logger.error(f"Sending images from: {IMAGES_PATH}")

    serve(app, host='0.0.0.0', port=5000)
