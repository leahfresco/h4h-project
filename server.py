from jinja2 import StrictUndefined
from flask_debugtoolbar import DebugToolbarExtension
from flask import Flask, render_template, redirect, request, flash, session, jsonify, g, url_for
from model import *
import os

app = Flask(__name__)

# Required to use Flask sessions and the debug toolbar
app.secret_key = "hackingnow"

# Raises an error for Jinja2 errors
app.jinja_env.undefined = StrictUndefined

# For Facebook OAUTH
app.config['OAUTH_CREDENTIALS'] = {
    'facebook': {
        'id': os.environ['FACEBOOK_API_ID'],
        'secret': os.environ['FACEBOOK_SECRET_ID']
    }
}

@app.route('/')
def index():
    """Homepage."""
    return render_template("index.html")


if __name__ == "__main__":
    # We have to set debug=True here, since it has to be True at the
    # point that we invoke the DebugToolbarExtension
    app.debug = True
    app.jinja_env.auto_reload = app.debug  # make sure templates, etc. are not cached in debug mode

    connect_to_db(app, 'postgresql:///h4hproject')

    app.run(port=5000, host='0.0.0.0')