from random import seed, randint
from notly import app
from flask import send_from_directory

class FileService:

    def save_file(self, file):
        file_id = "{}.pdf".format(randint(100000000, 999999999))
        file.save(app.config['UPLOAD_FOLDER'] + file_id)
        return file_id

    def get_gile(self, file_id):
        return send_from_directory(app.config['UPLOAD_FOLDER'], file_id)