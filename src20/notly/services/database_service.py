import sqlite3
from time import time
from notly import app
from notly.config import DatabasePath


class NotlyDbService:
    db_path = None

    def __init__(self, user):
        self.user = user
        self.db_path = DatabasePath.Notly

    def __enter__(self):
        self._get_connection_and_cursor()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.cursor.close()
        self.connection.close()

    def make_dicts(self, row):
        return dict((self.cursor.description[idx][0], value)
                    for idx, value in enumerate(row))

    def _get_connection_and_cursor(self):
        # app.logger.info("Opening database with path: {}".format(self.db_path))
        self.connection = sqlite3.connect(self.db_path)
        self.cursor = self.connection.cursor()

    def get_epoches(self):
        self.cursor.execute("SELECT * FROM epoches")
        epoches = self.cursor.fetchall()
        return [dict(zip([cursor[0] for cursor in self.cursor.description], epoch)) for epoch in epoches]
