from flask import send_from_directory, session, render_template
from notly import app
from notly.services.artist_service import ArtistService
from notly.services.epoch_service import EpochService
from notly.services.song_service import SongService

@app.route('/artist/<string:artist_href>', methods=['GET'])
def get_artist(artist_href):
    return render_template(
        'single_artist.html',
        artist=ArtistService().get_artist_by_href(artist_href),
        epoch=EpochService().get_epoch_by_artist_href(artist_href),
        songs=SongService().get_songs_by_artist_href(artist_href))
