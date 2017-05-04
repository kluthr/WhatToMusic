import sys
import json
from flask import Flask
from flask import render_template
from flask import jsonify
from cStringIO import StringIO
from verse import Verse
from flask import request
from time import time

app = Flask(__name__)
    
@app.route('/')
def index():
    return render_template("jambot.html")

@app.route('/create')
def create():
    song = None
    song = Verse(time())
    old_stdout = sys.stdout
    sys.stdout = mystdout = StringIO()
    song.print_verse()
    sys.stdout = old_stdout
    sys.stdout.flush()
    return jsonify(notation=mystdout.getvalue(), url=song.url)

@app.after_request
def add_header(r):
    r.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    r.headers["Pragma"] = "no-cache"
    r.headers["Expires"] = "0"
    r.headers['Cache-Control'] = 'public, max-age=0'
    return r

if __name__ == "__main__":
    app.run(debug=True)
