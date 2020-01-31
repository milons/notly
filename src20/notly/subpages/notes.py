from flask import send_from_directory, session, render_template, request
from notly import app
from notly.services.note_service import NoteService
from notly.services.credential_service import login_required

@app.route('/note/download/<int:file_id>', methods=['GET'])
# @login_required
def download_note(file_id):
    return "It works!"

@app.route('/note/upload', methods=['POST'])
# @login_required
def upload_note():
    if request.method == 'POST':
        f = request.files['file']
        f.save(f.filename)
        return "Uploaded!"

