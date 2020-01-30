from notly import app
from functools import wraps
from flask import session, redirect, url_for

def login_required(f):
    @wraps(f)
    def function(*args, **kwargs):
        if 'user' not in session:
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    return function