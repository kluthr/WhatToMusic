import random
#import pyaudio
from macros import *
from key import Key

class Melody(object):

    def __init__(self, measures, key_name, scale, key=None):
        self.measures = measures
        self.key = key if key else Key(key_name, scale)
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
