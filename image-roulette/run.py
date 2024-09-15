import os
import sys
import random
from flask import Flask, send_file, render_template, make_response

templates_folder = os.path.join(os.path.dirname(
    os.path.abspath(__file__)), "templates")

PERIOD_SECONDS = "600"

IMAGES_PATH = os.getenv("IMAGES_PATH")
if IMAGES_PATH is None or not os.path.isdir(IMAGES_PATH):
    IMAGES_PATH = "example"

PERIOD_SECONDS = os.getenv("PERIOD_SECONDS")
if PERIOD_SECONDS is None:
    PERIOD_SECONDS = 600
else:
    PERIOD_SECONDS = int(PERIOD_SECONDS)

CUSTOM_HTML = os.getenv("CUSTOM_HTML")
if CUSTOM_HTML is None:
    CUSTOM_HTML = ""
elif CUSTOM_HTML != "":
    CUSTOM_HTML = os.path.abspath(CUSTOM_HTML)

CUSTOM_HTML_LINK = os.path.join(templates_folder, "custom.html")
if os.path.islink(CUSTOM_HTML_LINK):
    os.remove(CUSTOM_HTML_LINK)

print("Settings:")
print(f"IMAGES_PATH:    {IMAGES_PATH}")
print(f"PERIOD_SECONDS: {PERIOD_SECONDS}")
print(f"CUSTOM_HTML:    {CUSTOM_HTML}")
app = Flask(__name__, static_folder=IMAGES_PATH)

@app.route('/')
@app.route('/random')
def _random():
    # Get a list of all the picture files in the folder
    images = [f for f in os.listdir(
        IMAGES_PATH) if f.lower().endswith(('.jpg', '.jpeg', '.png'))]

    template = "random.html"
    if os.path.exists(CUSTOM_HTML):
        if not os.path.exists(CUSTOM_HTML_LINK):
            os.symlink(CUSTOM_HTML, CUSTOM_HTML_LINK)
            print("Created custom.html link")
        template = "custom.html"

    header = render_template("header.html", images=images, period_seconds=PERIOD_SECONDS)

    return render_template(template, images=images, period_seconds=PERIOD_SECONDS, header=header)


if __name__ == '__main__':
    from waitress import serve
    import logging
    logger = logging.getLogger("waitress")
    logger.setLevel(logging.INFO)
    serve(app, host='0.0.0.0', port=5000)
