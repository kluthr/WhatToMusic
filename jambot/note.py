import numpy
import math
#import pyaudio

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

    def chunk_note(self):
        chunks = []
        chunks.append(self.sine())
        chunk = numpy.concatenate(chunks) * 0.25
        return chunk.astype(numpy.float32).tostring()
