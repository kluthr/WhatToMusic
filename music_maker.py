#!/usr/bin/python
#coding=utf-8

import numpy
import random
import math
import pyaudio
import sys
import os
from time import sleep
from macros import *


# set key like: "A4" or "B#6", 
# numbers = 4, 5, or 6,
# use sharp for # and flat,


class Note(object):

    def __init__(self, frequency=440, duration=1, amplitude=1,
                 rate=44100):
        self.frequency = frequency
        self.duration = duration
        self.amplitude = amplitude
        self.rate = rate

    def sine(self):
        length = float(self.duration * self.rate)
        factor = float(self.frequency) * ((math.pi * 2) / self.rate)
        return numpy.sin(numpy.arange(length) * factor)

    def play_note(self, stream):
        chunks = []
        chunks.append(self.sine())
        chunk = numpy.concatenate(chunks) * 0.25
        stream.write(chunk.astype(numpy.float32).tostring())

class Key(object):

    def __init__(self, name=None, scale_name=None):
        self.name = name
        self.scale_name = scale_name if scale_name else self.set_scale_name()
        self.scale = self.set_scale()
        self.notes = self.set_notes()

    def set_scale_name(self):
        return random.choice(list(SCALES))

    def set_scale(self):
        return SCALES[self.scale_name]

    def set_notes(self):
        notes = [self.name]
        index = NAMES.index(self.name)
        for step in self.scale:
            index += step
            if index > 11:
                index -= 12
            notes.append(NAMES[index])
        return notes

class Melody(object):

    def __init__(self, measures=4, key_name="C5", key=None):
        self.measures = measures
        self.key = key if key else Key(key_name)
        self.rhythm = self.set_rhythm()
        self.melody = self.set_melody()
    
 
    def set_rhythm(self):
        beats = []
        total = float(self.measures * MEASURE)
        while sum(beats) < total:
            beats.append(random.choice(BEATS))
        if sum(beats) > total:
            excess = sum(beats) - total
            beats[-1] = beats[-1] - excess
        return beats

    def set_melody(self):
        total = len(self.rhythm)
        order = []
        for position in range(total):
            name = random.choice(self.key.notes)
            order.append(name)
        return order

class Verse(object):
    
    def __init__(self, measures, key):
        self.frequencies = []
        self.first_melody = Melody(measures, key)
        self.second_melody = Melody(measures, self.first_melody.key.name,
                                     self.first_melody.key)
        self.note_arrangement = self.set_note_arrangement()
        self.beat_arrangement = self.set_beat_arrangement()
        self.frequencies = self.set_frequencies()

    def set_note_arrangement(self):
        return (self.first_melody.melody + self.first_melody.melody
                + self.second_melody.melody + self.first_melody.melody)

    def set_beat_arrangement(self):
        return (self.first_melody.rhythm + self.first_melody.rhythm
                +self.second_melody.rhythm + self.first_melody.rhythm)
    
    def set_frequencies(self):
        freqs = []
        for x in xrange(len(self.note_arrangement)):
            name = self.note_arrangement[x]
            note = Note(FREQUENCIES[name], self.beat_arrangement[x])
            freqs.append(note)
        return freqs

    def print_verse(self):
        break1 = len(self.first_melody.melody)
        break2 = break1 * 2
        break3 = break2 + len(self.second_melody.melody)
        print "Key of {}: {} scale".format(self.first_melody.key.name,
                                           self.first_melody.key.scale_name)
        for index in range(0, len(self.note_arrangement)):
            if index in (break1, break2, break3):
                print ""
            length = self.beat_arrangement[index]
            print "{}:{}".format(self.note_arrangement[index], length),
        print ""

    def play(self):
        p = pyaudio.PyAudio()
        stream = p.open(format=pyaudio.paFloat32, channels=1, rate=44100, output=1)
        self.print_verse()
        for note in self.frequencies:
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

# get key from user
# set up verse, chorus, bridge
# put together song (2 verse, chorus, 2 verse, chorus, bridge, chorus)
# print song
# play song
# repeat song?
# loop song?

# maybe: user sets structure
# fast/slow
# make new chorus/verse/bridge (keep other sections)
# write choruse/verse/bridge with keyboard
# build out to add chords?

# class break: length
# class melody: notes in order
# class song: verse, chorus, bridge, arrangement, key

if __name__ == "__main__":
    block_warning_before()
    verse = Verse(4, "C5")
    verse.play()
    block_warning_after()
