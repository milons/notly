from flask import send_from_directory, session, render_template
from notly import app
from notly.services.database_service import NotlyDbService


@app.route('/epoches', methods=['GET'])
def get_all_epoches():
    return render_template(
        'epoches.html',
        epoches=Epoch().get_epoches())


@app.route('/epoch/<string:epoch_href>', methods=['GET'])
def get_epoch(epoch_href):
    return render_template(
        'single_epoch.html',
        epoch=Epoch().get_epoch(epoch_href),
        artists=Epoch().get_artists_by_epoch(epoch_href),
        songs=Epoch().get_top_songs_by_epoch(epoch_href, 10))


class Epoch:
    def __init__(self):
        # self.user = session['user']
        self.notly_db_handler = NotlyDbService()

    def get_epoches(self):
        with self.notly_db_handler as notly_db:
            return notly_db.get_epoches()

    def get_epoch(self, epoch_href):
        with self.notly_db_handler as notly_db:
            return notly_db.get_epoch(epoch_href)

    def get_artists_by_epoch(self, epoch_href):
        with self.notly_db_handler as notly_db:
            return notly_db.get_artists_by_epoch(epoch_href)

    def get_top_songs_by_epoch(self, epoch_href, limit):
        with self.notly_db_handler as notly_db:
            return notly_db.get_top_songs_by_epoch(epoch_href, limit)
