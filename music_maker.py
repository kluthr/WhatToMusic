#!/usr/bin/python
#coding=utf-8

import numpy
import random
import math
import pyaudio
import sys
import os
from time import sleep


NAMES = ["A", "A#", "B", "C", "C#", "D", "D#", "E", "F", "F#", "G", "G#"]

FREQUENCIES = {
    "A": 440.0,
    "A#": 466.16,
    "B" : 493.88,
    "C": 523.25,
    "C#": 554.37,
    "D": 587.33,
    "D#": 622.25,
    "E": 659.25,
    "F": 698.46,
    "F#": 739.99,
    "G": 783.99,
    "G#": 830.61,
}

BEATS = [1, .75, .5, .25, .125]

MEASURE = 1

MAJOR = [2, 2, 1, 2, 2, 2]

class Note(object):

    def __init__(self, frequency=440, length=1, amplitude=1,
                 rate=44100):
        self.frequency = frequency
        self.length = length
        self.amplitude = amplitude
        self.rate = rate

    def sine(self):
        length = int(self.length * self.rate)
        factor = float(self.frequency) * (math.pi * 2) / self.rate
        return numpy.sin(numpy.arange(length) * factor)

    def play_note(self, stream):
        chunks = []
        chunks.append(self.sine())
        chunk = numpy.concatenate(chunks) * 0.25
        stream.write(chunk.astype(numpy.float32).tostring())

class Melody(object):

    def __init__(self, measures=4, key="C"):
        self.measures = measures
        self.key = key
        self.rhythm = []
        self.notes = []
        self.options = []
        self.melody = []
        self.set_rhythm()
        self.set_options()
        self.set_notes()
     
    def print_melody(self):
        for index in range(0, len(self.melody)):
            print "{}:{}".format(self.melody[index], self.rhythm[index]),
        print ""   
 
    def set_rhythm(self):
        total = float(self.measures * MEASURE)
        while sum(self.rhythm) < total:
            self.rhythm.append(random.choice(BEATS))
        if sum(self.rhythm) > total:
            excess = sum(self.rhythm) - total
            self.rhythm[-1] = self.rhythm[-1] - excess

    def set_options(self):
        self.options.append(self.key)
        index = NAMES.index(self.key)
        for step in MAJOR:
            index += step
            if index > 11:
                index -= 12
            self.options.append(NAMES[index])

    def set_notes(self):
        total = len(self.rhythm)
        start = NAMES.index(self.key)
        for position in range(total):
            name = random.choice(self.options)
            note = Note(FREQUENCIES[name], self.rhythm[position-1])
            self.notes.append(note)
            self.melody.append(name)

    def play(self):
        p = pyaudio.PyAudio()
        stream = p.open(format=pyaudio.paFloat32, channels=1, rate=44100, output=1)
        self.print_melody()
        for note in self.notes:
            note.play_note(stream)
            sleep(0.1)
        stream.close()
        p.terminate

def block_warning_before():
    devnull = os.open(os.devnull, os.O_WRONLY)
    old_stderr = os.dup(2)
    sys.stderr.flush()
    os.dup2(devnull, 2)
    os.close(devnull)

def block_warning_after():
    os.dup2(old_stderr, 2)
    os.close(old_stderr)
# get key
# set up possible notes (frequency, amp, whatevs)
# set up verse, chorus, bridge
# create rhythm for verse, chorus, bridge
# generate notes for verse, chorus, bridge
# put together song (2 verse, chorus, 2 verse, chorus, bridge, chorus)
# print song
# play song
# repeat song?
# loop song?

# maybe: user sets structure
# happy/sad (major, minor)
# fast/slow
# make new chorus/verse/bridge (keep other sections)
# write choruse/verse/bridge with keyboard
# build out to add chords?

# class break: length
# class melody: notes in order
# class song: verse, chorus, bridge, arrangement, key
# class key: notes, chords?, major/minor

# major key: W W H W W W H, the name is the starting note, one index step == half step in NAMES
# minor key: W H W W H W W

if __name__ == "__main__":
    melody = Melody(4, "C")
    print "Key of C:"
    block_warning_before()
    melody.play()
    melody.play()
    melody2 = Melody(4, "C")
    melody2.play()
    melody.play()
    block_warning_after()
