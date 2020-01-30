from flask import send_from_directory, session, render_template
from notly import app
from notly.services.epoch_service import EpochService
from notly.services.artist_service import ArtistService
from notly.services.song_service import SongService
from notly.subpages.epoches import get_all_epoches


@app.route('/login', methods=['GET'])
def get_login_page():
    if 'user' in session:
        return get_all_epoches()
    return render_template('login.html')