from flask import session, redirect
from notly import app

@app.route('/sign-off', methods=['GET'])
def sign_off(message=None):
    session.clear()
    return redirect('/')
    