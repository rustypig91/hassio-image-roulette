import os
from flask import Flask, render_template, render_template_string, abort
import jinja2

TEMPLATES_FOLDER = os.getenv("TEMPLATES_FOLDER")
if TEMPLATES_FOLDER is None or TEMPLATES_FOLDER == "":
    TEMPLATES_FOLDER = os.path.join(os.path.dirname(
        os.path.abspath(__file__)), "templates")

IMAGES_PATH = os.getenv("IMAGES_PATH")
if IMAGES_PATH is None or not os.path.isdir(IMAGES_PATH):
    IMAGES_PATH = "example"

PERIOD_SECONDS = os.getenv("PERIOD_SECONDS")
if PERIOD_SECONDS is None or PERIOD_SECONDS == "":
    PERIOD_SECONDS = 600
else:
    PERIOD_SECONDS = int(PERIOD_SECONDS)

app = Flask(__name__, static_folder=IMAGES_PATH,
            template_folder=TEMPLATES_FOLDER)

HEADER = """
<title>Image Roulette</title>
<script>
    var previousIndex = -1;
    var images = [{% for image in images %} '{{ url_for('static', filename=image) }}', {% endfor %}];

    function changeBackground() {
        var randomIndex = Math.floor(Math.random() * images.length);

        // Ensure the same random number is not chosen two times in a row
        while (randomIndex === previousIndex) {
            randomIndex = Math.floor(Math.random() * images.length);
        }

        previousIndex = randomIndex;
        console.log("Changing background to " + images[randomIndex]);
        var imageUrl = images[randomIndex];
        document.body.style.backgroundImage = 'url(' + imageUrl + ')';
    }
    window.onload = changeBackground;
    setInterval(changeBackground, {{period_seconds * 1000}});
</script>
<style>
    body, html {
        height: 100%;
        background-position: center;
        background-repeat: no-repeat;
        background-size: cover;
        overflow: hidden;
    }
</style>
"""


@app.route('/')
@app.route('/random')
def _random():
    # Get a list of all the picture files in the folder
    images = [f for f in os.listdir(
        IMAGES_PATH) if f.lower().endswith(('.jpg', '.jpeg', '.png'))]

    header = render_template_string(
        HEADER, images=images, period_seconds=PERIOD_SECONDS)

    return render_template("index.html", images=images, period_seconds=PERIOD_SECONDS, header=header)


@app.route('/<path:path>')
def static_file(path):
    try:
        return render_template(path)
    except jinja2.exceptions.TemplateNotFound:
        abort(404, description="404 file not found")


if __name__ == '__main__':
    import waitress
    import logging
    logger = logging.getLogger("waitress")

    logging.basicConfig(level=logging.DEBUG)

    logger.info(f"IMAGES_PATH:      {IMAGES_PATH}")
    logger.info(f"PERIOD_SECONDS:   {PERIOD_SECONDS}")
    logger.info(f"TEMPLATES_FOLDER: {TEMPLATES_FOLDER}")

    app.config['TEMPLATES_AUTO_RELOAD'] = True
    waitress.serve(app, host='0.0.0.0', port=5000)
