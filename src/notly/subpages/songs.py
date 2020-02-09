from flask import send_from_directory, session, render_template
from notly import app
from notly.services.song_service import SongService
from notly.services.artist_service import ArtistService
from notly.services.note_service import NoteService

@app.route('/songs', methods=['GET'])
def get_top_songs():
    return render_template(
        'songs.html',
        songs=SongService().get_top_songs(10))

@app.route('/song/<int:song_id>', methods=['GET'])
def get_song_by_id(song_id, uploaded_message=None, error=None):
    return render_template(
        'single_song.html',
        song=SongService().get_song_by_id(song_id),
        artist=ArtistService().get_artist_by_song_id(song_id),
        notes=NoteService().get_notes_by_song_id(song_id),
        message=uploaded_message, 
        error=error)