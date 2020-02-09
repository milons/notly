import os
from flask import send_from_directory, render_template
from notly import app, sess
from notly.subpages import artists, epoches, login, notes, register, songs, signoff

@app.route('/', methods=['GET'])
def index():
    return render_template('main.html')


@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'), 'favicon.ico')

if __name__ == "__main__":
    sess.init_app(app)
    app.debug = True
    app.run()
