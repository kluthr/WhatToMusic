import json
from melody import Melody
from verse import Verse

class Importer(object):
    def __init__(self, input_file):
        self.input_file = input_file
        self.melodies = []
        self.verses = []
        self.scale = ''

    def read_songs(self):
        with open(self.input_file) as songs:
            data = json.load(songs)
            for song in data["songs"]:
               melody = Melody(4, song["key"], song["scale"])
               melody.rhythm = song["beats"]
               melody.melody = song["melody"]
               self.melodies.append(melody)
               self.scale = song["scale"]

    def make_verses(self):
        for melody in self.melodies:
            verse = Verse(4, melody.key.name, self.scale)
            verse.note_arrangement = melody.melody
            verse.beat_arrangement = melody.rhythm
            verse.set_frequencies()
            self.verses.append(verse)

    def play_verses(self):
        for verse in self.verses:
            verse.print_verse()
            verse.play()

def main():
    importer = Importer("jambot_songs2.json")
    importer.read_songs()
    importer.make_verses()
    print "Imported {} songs!".format(len(importer.verses))
    choice = int(raw_input("Which song do you want to hear? (Enter 0 for all)\
        "))
    if 0 < choice <= len(importer.verses):
       if choice == 0:
           importer.play_verses()
       else:
           choice -= 1
           importer.verses[choice].print_verse()
           importer.verses[choice].play()
    else: 
        "Bad song number!"


if __name__=="__main__":
    main()
