from notly.services.database_service import NotlyDbService

class NoteService:
    def __init__(self):
        # self.user = session['user']
        self.notly_db_handler = NotlyDbService()
    
    def new_note(self, song_id, file_name):
        with self.notly_db_handler as notly_db:
            return notly_db.new_note(song_id, file_name)

    def get_notes_by_song_id(self, song_id):
        with self.notly_db_handler as notly_db:
            return notly_db.get_notes_by_song_id(song_id)