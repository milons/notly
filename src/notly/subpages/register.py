from flask import session, render_template, request, redirect
from notly import app
from notly.services.credential_service import CredentialService

@app.route('/register', methods=['GET'])
def get_register_page(message=None):
    if 'user' in session:
        return redirect('/')
    return render_template('register.html',
        message=message)

@app.route('/register/process', methods=['POST'])
def process_register():
    req_form = request.form.to_dict()
    register_result = CredentialService().process_register(req_form)
    if (register_result):
        return get_register_page(register_result)
    CredentialService().process_login(req_form)
    return redirect('/')