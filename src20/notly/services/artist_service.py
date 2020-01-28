from notly.services.database_service import NotlyDbService

class ArtistService:
    def __init__(self):
        # self.user = session['user']
        self.notly_db_handler = NotlyDbService()

    def get_song_by_id(self, song_id):
        with self.notly_db_handler as notly_db:
            return notly_db.get_song_by_id(song_id)

    def get_artists_by_epoch(self, epoch_href):
        with self.notly_db_handler as notly_db:
            return notly_db.get_artists_by_epoch(epoch_href)

    