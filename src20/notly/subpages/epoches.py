from flask import send_from_directory, session, render_template
from notly import app
from notly.services.database_service import NotlyDbService
from notly.services.epoch_service import EpochService
from notly.services.artist_service import ArtistService
from notly.services.song_service import SongService



@app.route('/epoches', methods=['GET'])
def get_all_epoches():
    return render_template(
        'epoches.html',
        epoches=EpochService().get_epoches())


@app.route('/epoch/<string:epoch_href>', methods=['GET'])
def get_epoch(epoch_href):
    return render_template(
        'single_epoch.html',
        epoch=EpochService().get_epoch(epoch_href),
        artists=ArtistService().get_artists_by_epoch(epoch_href),
        songs=SongService().get_top_songs_by_epoch(epoch_href, 10))