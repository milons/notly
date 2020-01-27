import os
from flask import Flask
from flask_session import Session
from logging.config import dictConfig


app = Flask(__name__)


app.secret_key = os.urandom(16)
app.config['SESSION_TYPE'] = 'filesystem'

sess = Session()
import notly.common

dictConfig({
    'version': 1,
    'formatters': {'default': {
        'format': '[%(asctime)s] %(levelname)s in %(module)s: %(message)s',
    }},
    'handlers': {'wsgi': {
        'class': 'logging.StreamHandler',
        'stream': 'ext://flask.logging.wsgi_errors_stream',
        'formatter': 'default'
    }},
    'root': {
        'level': 'INFO',
        'handlers': ['wsgi']
    }
})
