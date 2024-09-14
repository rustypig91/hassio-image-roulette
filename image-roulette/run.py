import os
import sys
import random
from flask import Flask, send_file, render_template, make_response

templates_folder = os.path.join(os.path.dirname(
    os.path.abspath(__file__)), "templates")

IMAGES_PATH = os.getenv("IMAGES_PATH")
if (IMAGES_PATH is None) or (not os.path.isdir(IMAGES_PATH)):
    IMAGES_PATH = "example"

PERIOD_SECONDS = os.getenv("PERIOD_SECONDS")
if (PERIOD_SECONDS is None):
    PERIOD_SECONDS = 600


custom_script = os.path.join(IMAGES_PATH, "custom.py")
if (os.path.exists(custom_script)):
    sys.path.append(IMAGES_PATH)
    from custom import custom_body  # type: ignore
    custom_html = os.path.join(IMAGES_PATH, "custom.html")
    if os.path.exists(custom_html):
        if os.path.islink(os.path.join(templates_folder, "custom.html")):
            os.remove(os.path.join(templates_folder, "custom.html"))
        os.symlink(os.path.abspath(custom_html),
                   os.path.join(templates_folder, "custom.html"))
else:
    def custom_body():
        return ""

app = Flask(__name__, static_folder=IMAGES_PATH,
            template_folder=templates_folder)


@app.route('/random')
def serve_random_picture():
    # if IMAGES_PATH is None:
    #     response = make_response("Images path not setup", 200)
    #     response.mimetype = "text/plain"
    #     return response

    # Get a list of all the picture files in the folder
    picture_files = [file for file in os.listdir(
        IMAGES_PATH) if file.lower().endswith(('.jpg', '.jpeg', '.png'))]
    # raise Exception(picture_files)
    if len(picture_files) == 0:
        return f"No images found in image path ({IMAGES_PATH})"
    # Choose a random picture from the list
    random_picture = random.choice(picture_files)

    return render_template('random.html', random_picture=random_picture, pictures=picture_files, period_seconds=PERIOD_SECONDS, custom_body=custom_body())
    # # Return the picture file
    # return send_file(os.path.join(IMAGES_PATH, random_picture))


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
