import flask

from google.appengine.ext import blobstore


app = flask.Flask('pixie_land')


@app.route('/')
def index():
    return """
        <h1>Upload your magic to pixie land!</h1>
        <form method='POST' action='{url}'>
            <input type='file' name='fairydust' />
            <input type='submit' />
        </form>
    """.format(url=blobstore.create_upload_url(flask.url_for('upload')))


@app.route('/gimme-upload-url/')
def gimme_upload_url():
    """
    Helper view so that `upload_the_magic.sh` can get a `/_ah/upload` url.
    """
    return blobstore.create_upload_url(flask.url_for('upload'))


@app.route('/upload/', methods=['POST'])
def upload():
    return "YOU UPLOADED. PIXIE LAND IS SAVED."

