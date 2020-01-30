from notly.services.database_service import NotlyDbService

class NoteService:
    def __init__(self):
        # self.user = session['user']
        self.notly_db_handler = NotlyDbService()