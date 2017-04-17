import pyaudio
from time import sleep
from macros import *
from note import Note
from melody import Melody

class Verse(object):
    
    def __init__(self, measures, key_name, scale):
        self.frequencies = []
        self.first_melody = Melody(measures, key_name, scale)
        self.second_melody = Melody(measures, key_name, scale, self.first_melody.key)
        self.note_arrangement = self.set_note_arrangement()
        self.beat_arrangement = self.set_beat_arrangement()
        self.frequencies = self.set_frequencies()

    def set_note_arrangement(self):
        return (self.first_melody.melody + self.first_melody.melody
                + self.second_melody.melody + self.first_melody.melody)

    def set_beat_arrangement(self):
        return (self.first_melody.rhythm + self.first_melody.rhythm
                + self.second_melody.rhythm + self.first_melody.rhythm)
    
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