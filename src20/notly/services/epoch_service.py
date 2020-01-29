from notly.services.database_service import NotlyDbService

class EpochService:
    def __init__(self):
        # self.user = session['user']
        self.notly_db_handler = NotlyDbService()

    def get_epoches(self):
        with self.notly_db_handler as notly_db:
            return notly_db.get_epoches()

    def get_epoch(self, epoch_href):
        with self.notly_db_handler as notly_db:
            return notly_db.get_epoch(epoch_href)

    def get_epoch_by_artist_href(self, artist_href):
        with self.notly_db_handler as notly_db:
            return notly_db.get_epoch_by_artist_href(artist_href)