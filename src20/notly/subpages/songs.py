from flask import send_from_directory, session, render_template
from notly import app
from notly.services.song_service import SongService
from notly.services.artist_service import ArtistService


@app.route('/song/<int:song_id>', methods=['GET'])
def get_song_by_id(song_id):
    return render_template(
        'single_song.html',
        song=SongService().get_song_by_id(song_id),
        artist=ArtistService().get_artist_by_song_id(song_id))