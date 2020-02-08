from flask import session

def user_logged():
    return 'user' in session