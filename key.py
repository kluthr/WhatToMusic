import random
from macros import *

class Key(object):

    def __init__(self, name, scale_name):
        self.name = name
        self.scale_name = scale_name     #if scale_name else self.set_scale_name()
        self.scale = self.set_scale()
        self.notes = self.set_notes()

    #def set_scale_name(self):
    #   return random.choice(list(SCALES))

    def set_scale(self):
        return SCALES[self.scale_name]

    def set_notes(self):
        notes = [self.name]
        print self.name
        print NAMES
        index = NAMES.index(self.name)
        for step in self.scale:
            index += step
            if index > 11:
                index -= 12
            notes.append(NAMES[index])
        return notes