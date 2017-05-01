import pyaudio
import wave
from pydub import AudioSegment
from time import time, sleep
from macros import *
from random import choice
from note import Note
from melody import Melody

TIME = str(time())[:-3]
WAV = 'static/songs/' + TIME + '.wav'
MP3 = 'static/songs/' + TIME + '.mp3'
URL = 'http://52.42.87.255/' + MP3

class Verse(object):
    
    def __init__(self, measures=None, key=None, scale=None, m1=None, m2=None,
                 notes=None, beats=None):
        self.key = key if key else choice(NAMES)            
        self.scale = scale if scale else choice(list(SCALES))
        self.measures = measures if measures else 4 
        self.first_melody = m1 if m1 else Melody(self.measures, self.key,
                                                 self.scale)
        self.second_melody = m2 if m2 else Melody(self.measures, self.key,
                                                  self.scale,
                                                  self.first_melody.key)
        self.note_arrangement = notes if notes else self.set_note_arrangement()
        self.beat_arrangement = beats if beats else self.set_beat_arrangement()
        self.frequencies = self.set_frequencies()
        self.songwave = ''
        self.url = URL
        self.record()
        self.convert()

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
        print "Key of {}<br>> {} Scale<br>".format(self.first_melody.key.name,
                                           self.first_melody.key.scale_name)
        print ">"
        for index in range(0, len(self.note_arrangement)):
            if index in (break1, break2, break3):
                print "<br>>"
            length = self.beat_arrangement[index]
            print " {}({}) ".format(self.note_arrangement[index][:-1], length),
        print ""

    def record(self):
        with open(WAV, 'w+'):
            prev = Note(0)
            for note in self.frequencies:
                if note == prev:
                    silence = Note(0, 0.125)
                    self.songwave += note.chunk_note()
                self.songwave += note.chunk_note()
                prev = note
            end = Note(0, 1.0)
            self.songwave += note.chunk_note()
        wf = wave.open(WAV, 'wb')
        wf.setnchannels(1)
        wf.setsampwidth(4.0)
        wf.setframerate(44100)
        wf.writeframes(self.songwave)
        wf.close()

    def convert(self):
        with open(MP3, 'w+'):
            pass
        song = AudioSegment.from_wav(WAV)
        song.export(MP3, format='mp3')

#    def play(self):
#        p = pyaudio.PyAudio()
#        stream = p.open(format=pyaudio.paFloat32, channels=1, rate=44100,
#                        output=True)
#        stream.write(self.songwave)
#        sleep(1)
 #       stream.close()
  #      p.terminate
