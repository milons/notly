from flask import session, render_template, request, redirect
from notly import app
from notly.services.credential_service import CredentialService

@app.route('/login', methods=['GET'])
def get_login_page(message=None):
    if 'user' in session:
        return redirect('/')
    return render_template('login.html',
        message=message)

@app.route('/login/process', methods=['POST'])
def process_login():
    req_form = request.form.to_dict()
    login_result = CredentialService().process_login(req_form)
    if (login_result):
        return get_login_page(login_result)
    return redirect('/')