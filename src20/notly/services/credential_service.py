from notly import app
from functools import wraps
from flask import session, redirect, url_for
from notly.services.database_service import NotlyDbService
import hashlib

class CredentialService:

    def process_login(self, login_dict):
        login = login_dict['login']
        password = login_dict['password']
        hash_password = hashlib.sha3_384(password.encode()).hexdigest()
        
        with NotlyDbService() as notly_db:
            name = notly_db.verify_user_credential(login, hash_password)
            if (len(name) > 0):
                session['user'] = name
            else:
                return 'Invalid login or password'
             

    def process_register(self, register_dict):
        login = register_dict['login']
        if (len(login) == 0):
            return 'Login empty.'
        name = register_dict['name']
        if (len(name) == 0):
            return 'Name empty.'
        password = register_dict['password']
        if (len(password) == 0):
            return 'Password empty.'
        
        hash_password = hashlib.sha3_384(password.encode()).hexdigest()
        with NotlyDbService() as notly_db:
            exists = notly_db.user_exists(login)
            if (exists > 0):
                return 'Login is use.'
            notly_db.register_user(login, hash_password, name)

def login_required(f):
    @wraps(f)
    def function(*args, **kwargs):
        if 'user' not in session:
            return redirect(url_for('get_login_page'))
        return f(*args, **kwargs)
    return function