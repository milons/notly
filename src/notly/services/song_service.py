from notly.services.database_service import NotlyDbService

class SongService:
    def __init__(self):
        self.notly_db_handler = NotlyDbService()

    def get_song_by_id(self, song_id):
        with self.notly_db_handler as notly_db:
            return notly_db.get_song_by_id(song_id)

    def get_top_songs_by_epoch(self, epoch_href, limit):
        with self.notly_db_handler as notly_db:
            return notly_db.get_top_songs_by_epoch(epoch_href, limit)
    
    def get_songs_by_artist_href(self, artist_href):
        with self.notly_db_handler as notly_db:
            return notly_db.get_songs_by_artist_href(artist_href)
    
    def get_top_songs(self, limit):
        with self.notly_db_handler as notly_db:
            return notly_db.get_top_songs(limit)