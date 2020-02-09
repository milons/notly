from flask import send_from_directory, session, render_template, request, redirect
from notly import app
from notly.services.epoch_service import EpochService
from notly.services.artist_service import ArtistService
from notly.services.song_service import SongService
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