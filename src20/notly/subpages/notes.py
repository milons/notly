from flask import send_from_directory, session, render_template
from notly import app
from notly.services.note_service import NoteService
from notly.services.credential_service import login_required

@app.route('/download-note/<int:file_id>', methods=['GET'])
@login_required
def download_note(file_id):
    return "It works!"


