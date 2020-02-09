import os
from flask import Flask
from flask_session import Session
from notly.services.common_service import user_logged

app = Flask(__name__)
app.secret_key = os.urandom(16)
app.config['SESSION_TYPE'] = 'filesystem'
app.config['UPLOAD_FOLDER'] = app.config.root_path + '/_notes_files/'

sess = Session()

import notly.common
app.jinja_env.globals.update(user_logged=user_logged)
