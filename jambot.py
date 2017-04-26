import sys
from flask import Flask
from flask import render_template
from flask import jsonify
from cStringIO import StringIO
from verse import Verse
from flask import g

app = Flask(__name__)

def after_this_request(func):
    if not hasattr(g, 'call_after_request'):
        g.call_after_request = []
    g.call_after_request.append(func)
    return func

@app.after_request
def per_request_callbacks(response):
    for func in getattr(g, 'call_after_request', ()):
        response = func(response)
    return response

@app.route('/')
def index():
    return render_template("jambot.html")

@app.route('/sing')
def sing():
    song = Verse()
    old_stdout = sys.stdout
    sys.stdout = mystdout = StringIO()
    song.print_verse()
    sys.stdout = old_stdout    
    song.play()
    return jsonify(song=mystdout.getvalue())

app.run(debug=True, port=8000, host='0.0.0.0')
