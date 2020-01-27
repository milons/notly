from flask import send_from_directory, session, render_template
from notly import app
from notly.services import *

@app.route('/epoches', methods=['GET'])
def get_all_epoches():
  return render_template(
      'epoches.html', 
      epoches = Epoch.get_epoches())


class Epoch:
    def __init__(self):
        self.user = session['user']
        self.notly_db_handler = NotlyDbService(self.user)
        self.epoches = None

    def get_epoches(self):
        with self.notly_db_handler as notly_db:
            self.epoches = notly_db.get_epoches()
        return self.epoches