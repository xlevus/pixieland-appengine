import flask

app = flask.Flask('default')


@app.route('/')
def index():
    return "I'M THE DEFAULT MODULE. I AM EVIL."


@app.route('/upload/', methods=['POST'])
def upload():
    return "YOU GAVE THE MAGIC TO MR-EVIL. GOODBYE UNICORNS", 404
