from flask import send_from_directory, session, render_template, request, redirect
from notly import app
from notly.services.epoch_service import EpochService
from notly.services.artist_service import ArtistService
from notly.services.song_service import SongService
from notly.services.credential_service import CredentialService

@app.route('/sign-off', methods=['GET'])
def sign_off(message=None):
    session.clear()
    return redirect('/')
    