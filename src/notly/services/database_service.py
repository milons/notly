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
        self.connection = sqlite3.connect(self.db_path.value)
        self.cursor = self.connection.cursor()

###### USERS ######


    def user_exists(self, login):
        request = \
            "SELECT COUNT(*) "\
            "FROM users u "\
            "WHERE u.login = '{}'".format(login)
        self.cursor.execute(request)
        collection = self.cursor.fetchall()
        return collection[0][0]

    def register_user(self, login, hash_password, name):
        request = \
            "INSERT INTO users(login, password_hash, name) "\
            "VALUES ('{}', '{}', '{}')".format(login, hash_password, name)
        self.cursor.execute(request)
        self.connection.commit()

    def verify_user_credential(self, login, password_hash):
        request = \
            "SELECT u.name "\
            "FROM users u "\
            "WHERE u.login = '{}' AND u.password_hash = '{}'".format(login, password_hash)
        self.cursor.execute(request)
        collection = self.cursor.fetchall()
        return [dict(zip([cursor[0] for cursor in self.cursor.description], element)) for element in collection][0]['name']

###### EPOCHES ######

    def get_epoches(self):
        self.cursor.execute(\
            "SELECT e.name, e.href, e.main_image, e.starting_year, e.ending_year "\
            "FROM epoches e")
        collection = self.cursor.fetchall()
        return [dict(zip([cursor[0] for cursor in self.cursor.description], element)) for element in collection]

    def get_epoch(self, epoch_href):
        request = \
            "SELECT e.href, e.name, e.main_image, e.starting_year, e.ending_year "\
            "FROM epoches e "\
            "WHERE e.href = '{}'".format(epoch_href)
        self.cursor.execute(request)
        collection = self.cursor.fetchall()
        return [dict(zip([cursor[0] for cursor in self.cursor.description], element)) for element in collection][0]

    def get_epoch_with_description(self, epoch_href):
        request = \
            "SELECT e.href, e.name, e.main_image, e.full_description, e.starting_year, e.ending_year "\
            "FROM epoches e "\
            "WHERE e.href = '{}'".format(epoch_href)
        self.cursor.execute(request)
        collection = self.cursor.fetchall()
        return [dict(zip([cursor[0] for cursor in self.cursor.description], element)) for element in collection][0]


    def get_epoch_by_artist_href(self, artist_href):
        request = \
            "SELECT e.href, e.name, e.main_image, e.full_description, e.starting_year, e.ending_year "\
            "FROM epoches e "\
            "LEFT JOIN artists a "\
            "ON e.id = a.epoch_id "\
            "WHERE a.href = '{}'".format(artist_href)
        self.cursor.execute(request)
        collection = self.cursor.fetchall()
        return [dict(zip([cursor[0] for cursor in self.cursor.description], element)) for element in collection][0]

###### ARTISTS ######

    def get_top_artists(self):
        request = \
            "SELECT a.id, a.name, a.href, a.main_image, e.name as epoch_name "\
            "FROM artists a "\
            "LEFT JOIN epoches e "\
            "ON e.id = a.epoch_id "\
            "ORDER BY RANDOM() "\
            "LIMIT 9"
        self.cursor.execute(request)
        collection = self.cursor.fetchall()
        return [dict(zip([cursor[0] for cursor in self.cursor.description], element)) for element in collection]

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
            "SELECT a.name, a.main_image, a.href "\
            "FROM artists a "\
            "WHERE a.href = '{}'".format(artist_href)
        self.cursor.execute(request)
        collection = self.cursor.fetchall()
        return [dict(zip([cursor[0] for cursor in self.cursor.description], element)) for element in collection][0]

    def get_artist_with_description_by_href(self, artist_href):
        request = \
            "SELECT a.name, a.main_image, a.description, a.href "\
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

    def get_artist_by_song_id(self, song_id):
        request = \
            "SELECT a.name, a.href, a.main_image "\
            "FROM artists a "\
            "LEFT JOIN songs s "\
            "ON a.id = s.artist_id "\
            "WHERE s.id = '{}'".format(song_id)
        self.cursor.execute(request)
        collection = self.cursor.fetchall()
        return [dict(zip([cursor[0] for cursor in self.cursor.description], element)) for element in collection][0]

###### SONGS ######

    def get_top_songs(self, limit):
        request = \
            "SELECT s.id, a.name, s.title "\
            "FROM songs s "\
            "LEFT JOIN artists a "\
            "ON s.artist_id = a.id "\
            "ORDER BY RANDOM() "\
            "LIMIT {}".format(limit)
        self.cursor.execute(request)
        collection = self.cursor.fetchall()
        return [dict(zip([cursor[0] for cursor in self.cursor.description], element)) for element in collection]

    def get_top_songs_by_epoch(self, epoch_href, limit):
        request = \
            "SELECT s.id, a.name, s.title "\
            "FROM songs s "\
            "LEFT JOIN artists a "\
            "ON s.artist_id = a.id "\
            "LEFT JOIN epoches e "\
            "ON a.epoch_id = e.id "\
            "WHERE e.href = '{}' "\
            "ORDER BY RANDOM() "\
            "LIMIT {}".format(epoch_href, limit)
        self.cursor.execute(request)
        collection = self.cursor.fetchall()
        return [dict(zip([cursor[0] for cursor in self.cursor.description], element)) for element in collection]
    
    def get_song_by_id(self, song_id):
        request = \
            "SELECT s.id, s.title "\
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
    def new_note(self, song_id, file_name):
        request = \
            "INSERT INTO NOTES(song_id, file_name) "\
            "VALUES ({}, '{}')".format(song_id, file_name)
        self.cursor.execute(request)
        self.connection.commit()
    
    def get_notes_by_song_id(self, song_id):
        request = \
            "SELECT n.id, n.file_name "\
            "FROM notes n "\
            "LEFT JOIN songs s "\
            "ON s.id = n.song_id "\
            "WHERE s.id = '{}'".format(song_id)
        self.cursor.execute(request)
        collection = self.cursor.fetchall()
        return [dict(zip([cursor[0] for cursor in self.cursor.description], element)) for element in collection]

    def get_filename_by_id(self, song_id):
        request = \
            "SELECT n.file_name "\
            "FROM notes n "\
            "WHERE n.id = '{}'".format(song_id)
        self.cursor.execute(request)
        collection = self.cursor.fetchall()
        return [dict(zip([cursor[0] for cursor in self.cursor.description], element)) for element in collection][0]['file_name']