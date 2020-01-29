import sqlite3
from time import time
from notly import app
from notly.config import DatabasePath


class NotlyDbService:

    db_path = None

    def __init__(self):
        # self.user = user
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
        self.connection = sqlite3.connect(self.db_path.value)
        self.cursor = self.connection.cursor()

###### EPOCHES ######

    def get_epoches(self):
        self.cursor.execute(\
            "SELECT e.name, e.href, e.main_image, e.description, e.starting_year, e.ending_year "\
            "FROM epoches e")
        collection = self.cursor.fetchall()
        return [dict(zip([cursor[0] for cursor in self.cursor.description], element)) for element in collection]

    def get_epoch(self, epoch_href):
        request = \
            "SELECT e.name, e.main_image, e.full_description, e.starting_year, e.ending_year "\
            "FROM epoches e "\
            "WHERE e.href = '{}'".format(epoch_href)
        self.cursor.execute(request)
        collection = self.cursor.fetchall()
        return [dict(zip([cursor[0] for cursor in self.cursor.description], element)) for element in collection][0]

    def get_epoch_by_artist_href(self, artist_href):
        request = \
            "SELECT e.name, e.main_image, e.full_description, e.starting_year, e.ending_year "\
            "FROM epoches e "\
            "LEFT JOIN artists a "\
            "ON e.id = a.epoch_id "\
            "WHERE a.href = '{}'".format(artist_href)
        self.cursor.execute(request)
        collection = self.cursor.fetchall()
        return [dict(zip([cursor[0] for cursor in self.cursor.description], element)) for element in collection][0]

###### ARTISTS ######
    def get_artists_by_epoch(self, epoch_href):
        request = \
            "SELECT a.id, a.name, a.href, a.description, a.main_image "\
            "FROM artists a "\
            "LEFT JOIN epoches e "\
            "ON e.id = a.epoch_id "\
            "WHERE e.href = '{}'".format(epoch_href)
        self.cursor.execute(request)
        collection = self.cursor.fetchall()
        return [dict(zip([cursor[0] for cursor in self.cursor.description], element)) for element in collection]

    def get_artist_by_id(self, artist_id):
        request = \
            "SELECT a.name, a.main_image "\
            "FROM artists a "\
            "WHERE a.id = '{}'".format(artist_id)
        self.cursor.execute(request)
        collection = self.cursor.fetchall()
        return [dict(zip([cursor[0] for cursor in self.cursor.description], element)) for element in collection][0]

    def get_artist_by_href(self, artist_href):
        request = \
            "SELECT a.name, a.main_image "\
            "FROM artists a "\
            "WHERE a.href = '{}'".format(artist_href)
        self.cursor.execute(request)
        collection = self.cursor.fetchall()
        return [dict(zip([cursor[0] for cursor in self.cursor.description], element)) for element in collection][0]

    def get_full_artist_by_id(self, artist_id):
        request = \
            "SELECT a.name, a.description, a.href, a.main_image "\
            "FROM artists a "\
            "WHERE a.id = '{}'".format(artist_id)
        self.cursor.execute(request)
        collection = self.cursor.fetchall()
        return [dict(zip([cursor[0] for cursor in self.cursor.description], element)) for element in collection][0]

###### SONGS ######
    def get_top_songs_by_epoch(self, epoch_href, limit):
        request = \
            "SELECT s.id, a.name, s.title "\
            "FROM songs s "\
            "LEFT JOIN artists a "\
            "ON s.artist_id = a.id "\
            "LEFT JOIN epoches e "\
            "ON a.epoch_id = e.id "\
            "WHERE e.href = '{}' "\
            "LIMIT {}".format(epoch_href, limit)
        self.cursor.execute(request)
        collection = self.cursor.fetchall()
        return [dict(zip([cursor[0] for cursor in self.cursor.description], element)) for element in collection]
    
    def get_song_by_id(self, song_id):
        request = \
            "SELECT s.title "\
            "FROM songs s "\
            "WHERE s.id = '{}'".format(song_id)
        self.cursor.execute(request)
        collection = self.cursor.fetchall()
        return [dict(zip([cursor[0] for cursor in self.cursor.description], element)) for element in collection][0]

    def get_songs_by_artist_href(self, artist_href):
        request = \
            "SELECT s.id, s.title "\
            "FROM songs s "\
            "LEFT JOIN artists a "\
            "ON s.artist_id = a.id "\
            "WHERE a.href = '{}'".format(artist_href)
        self.cursor.execute(request)
        collection = self.cursor.fetchall()
        return [dict(zip([cursor[0] for cursor in self.cursor.description], element)) for element in collection]
###### NOTES ######