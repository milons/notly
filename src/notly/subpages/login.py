from flask import send_from_directory, session, render_template, request, redirect
from notly import app
from notly.services.epoch_service import EpochService
from notly.services.artist_service import ArtistService
from notly.services.song_service import SongService
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