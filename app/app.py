import os

from flask import Flask, redirect, render_template, request, url_for
from flask_bootstrap import Bootstrap
from werkzeug.utils import secure_filename

# Flask extensions
bootstrap = Bootstrap()

app = Flask(__name__)

# Initialize flask extensions
bootstrap.init_app(app)

# env vars for tmp purposes
class Config(object):
    # DEBUG = False
    # TESTING = False
    SECRET_KEY = os.environ.get('SECRET_KEY',
                                'superSecretDoNotUseOnOpenWeb')

# init config
app.config.from_object(Config)

@app.route('/')
def index():

    return render_template('home.html')

@app.route('/or')
def bio():

    me = url_for('static',
                      filename='images/me.jpg')
    return render_template('bio.html', me_url = me)

@app.route('/transfer-models')
def transfer_models():

    return render_template('transfer-models.html')
