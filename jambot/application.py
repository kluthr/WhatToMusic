import sys
import json
from flask import Flask
from flask import render_template
from flask import jsonify
from cStringIO import StringIO
from verse import Verse
from flask import request
from flask import send_file

application = Flask(__name__)

@application.route('/')
def index():
    return render_template("jambot.html")

@application.route('/create')
def create():
    song = Verse()
    old_stdout = sys.stdout
    sys.stdout = mystdout = StringIO()
    song.print_verse()
    sys.stdout = old_stdout
#    print_song = jsonify(mystdout.getvalue()) 
    verse = {"key": song.key, "scale": song.scale,
             "melody": song.note_arrangement, "beats": song.beat_arrangement}
    return jsonify(verse=verse, notation=mystdout.getvalue(), url=song.wavefile)

#@application.route('/play', methods = ['POST'])
#def play():
 #   data = json.loads(request.form.get("verse")) 
  #  song = Verse(4, data["key"], data["scale"], "placeholder", "placeholder",
#                 data["melody"], data["beats"])
#    path_to_file = 'output.wav'
   # return jsonify(song=song.wavefile)


  #return send_file(path_to_file, 
   #                  mimetype="audio/wav", 
    #                 as_attachment=True, 
     #                attachment_filename="output.wave")

#   song.play()    
#    return jsonify(verse=data)


if __name__ == "__main__":
    application.run(debug=True)
