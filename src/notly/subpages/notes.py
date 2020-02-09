from flask import send_from_directory, session, render_template, request
from notly import app
from notly.services.note_service import NoteService
from notly.services.credential_service import login_required
from notly.services.file_service import FileService
from notly.subpages.songs import get_song_by_id

@app.route('/note/download/<int:file_id>', methods=['GET'])
@login_required
def download_note(file_id):
    file_name = NoteService().get_filename_by_id(file_id)
    file = FileService().get_gile(file_name)
    return file

@app.route('/note/upload', methods=['POST'])
# @login_required
def upload_note():
    if request.method == 'POST':
        song_id = request.form['song-id']
        file = request.files['new-note']
        if (file.content_length > 0):
            file_name = FileService().save_file(file)
            NoteService().new_note(song_id, file_name)
            return get_song_by_id(song_id, uploaded_message='New note uploaded!')
        else:
            return get_song_by_id(song_id, error='No file added!')
            