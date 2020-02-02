from flask import send_from_directory, session, render_template, request
from notly import app
from notly.services.note_service import NoteService
from notly.services.credential_service import login_required
from notly.services.file_service import FileService
from notly.subpages.songs import get_song_by_id

@app.route('/note/download/<int:file_id>', methods=['GET'])
# @login_required
def download_note(file_id):
    file_name = FileService().get_filename_by_id(file_id)
    return send_from_directory(app.config['UPLOAD_FOLDER'], file_name)

@app.route('/note/upload', methods=['POST'])
# @login_required
def upload_note():
    if request.method == 'POST':
        file_name = FileService().save_file(request.files['new-note'])
        song_id = request.form['song-id']
        NoteService().new_note(song_id, file_name)
        return get_song_by_id(song_id, uploaded_message='New note uploaded!')

