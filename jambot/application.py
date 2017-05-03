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
    return jsonify(notation=mystdout.getvalue(), url=song.url)


#if __name__ == "__main__":
#    app.run(debug=True)
