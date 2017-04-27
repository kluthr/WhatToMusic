import sys
import json
from flask import Flask
from flask import render_template
from flask import jsonify
from cStringIO import StringIO
from verse import Verse
from flask import request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("jambot.html")

@app.route('/create')
def create():
    song = Verse()
    old_stdout = sys.stdout
    sys.stdout = mystdout = StringIO()
    song.print_verse()
    sys.stdout = old_stdout
    print_song = jsonify(mystdout.getvalue()) 
    verse = {"key": song.key, "scale": song.scale,
             "melody": song.note_arrangement, "beats": song.beat_arrangement}
    return jsonify(verse=verse, notation=mystdout.getvalue())
        
@app.route('/play', methods = ['POST'])
def play():
    data = json.loads(request.form.get("verse"))
    song = Verse(4, data["key"], data["scale"], "placeholder", "placeholder",
                 data["melody"], data["beats"])
    song.play()    
    return jsonify(verse=data)

app.run(debug=True, port=8000, host='0.0.0.0')
