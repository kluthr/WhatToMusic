"""jambot.py

Usage:
jambot.py [--key=<k>] [--scale=<s>] [--measures=<m>]
jambot.py -h | --help
Options:
 --help            Show this screen
 --key=<k>         Key in Letter+Sharp+Number format (ex: A#4), default is random
 --scale=<s>       Scale choice, default is random: major, natural minor, harmonic minor, melodic minor, dorian mode, mixolydian mode, ahava raba mode, pentatonic blues
 --measures=<m>    Number of measures per phrase, default is 4

"""

import sys
import os
from random import choice
from docopt import docopt
from macros import *
from verse import Verse

class CLI(object):

    def __init__(self, args):
        print args['--key']
        self.key = args['--key'] if args['--key'] else choice(NAMES)
        self.scale = args['--scale'] if args['--scale'] else choice(list(SCALES))
        self.measures = args['--measures'] if args['--measures'] else 4

    def block_warning_before():
        devnull = os.open(os.devnull, os.O_WRONLY)
        old_stderr = os.dup(2)
        sys.stderr.flush()
        os.dup2(devnull, 2)
        os.close(devnull)

    def block_warning_after():
        os.dup2(old_stderr, 2)
        os.close(old_stderr)

    @classmethod
    def run(cls):
        args = docopt(__doc__)
        cli = cls(args)
        #self.block_warning_before()
        verse = Verse(cli.measures, cli.key, cli.scale)
        verse.play()
        #self.block_warning_after()


if __name__ == "__main__":
    CLI.run()


# IDEAS FOR IMPROVEMENTS

# Make CLI interactive:
#    1. Ask for key, scale, measures
#    2. Present verse, ask to redo
#    3. Repeat for chorus and bridge
#    4. Set up/play whole song
#    5. Loop to start another song
#    6. Ask to print
#    7. Option to export to JSON
#    8. Option to import from JSON
#    9. Option to silence pyAudio warnings

# General:
#    1. Add breaks as a note
#    2. Add bpm as an option (multiply durations?)
#    3. Add musical typing for user to add their own hook/phrase
#    4. Add bass/chords?
#    5. Alter to sounds like an actual instrument
#    6. Expand range? Let user dictate range?
#    7. Give song a randomized name? Create song from user name?
#    8. Create option for happy vs sad song? Fast vs slow? Alter scale and speed accordingly

# Good Coding:
#    1. PEP8 it
#    2. Add testing

# MAKE A GUI AT beckykluth.com