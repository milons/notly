from flask import send_from_directory, session, render_template
from notly import app
from notly.services.database_service import NotlyDbService


@app.route('/song/<int:song_id>', methods=['GET'])
def get_song_by_id(song_id):
    return render_template(
        'single_song.html',
        song=Songs().get_song_by_id(song_id) # ,
        # artist=Artists().get_artist(song_id)
        )


class Songs:
    def __init__(self):
        # self.user = session['user']
        self.notly_db_handler = NotlyDbService()

    def get_song_by_id(self, song_id):
        with self.notly_db_handler as notly_db:
            return notly_db.get_song_by_id(song_id)


    