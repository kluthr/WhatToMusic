FREQUENCIES = {
    "A3": 220.00,
    "A#3": 233.08,
    "B3": 246.94,
    "C4": 261.63,
    "C#4": 277.18,
    "D4":293.66,
    "D#4": 311.13,
    "E4": 329.63,
    "F4": 349.23,
    "F#4": 369.99,
    "G4": 392.00,
    "G#4": 415.30,
    "A4": 440.00,
    "A#4": 466.16,
    "B4": 493.88,
#    "C5": 523.25,
#   "C#5":554.37,
#    "D5": 587.33,
#    "D#5": 622.25,
#    "E5": 659.25,
#    "F5": 698.46,
#    "F#5": 739.99,
#    "G5": 783.99,
#    "G#5": 830.61,
#    "A5": 880.00,
#    "A#5":932.33,
#    "B5": 987.77,
#    "C6": 1046.50,
#    "C#6": 1108.73,
#    "D6": 1174.66,
#    "D#6": 1244.51
    }

NAMES = list(FREQUENCIES)

BEATS = [1.0, 0.75, 0.5, 0.25, 0.125]

MEASURE = 1

SCALES = {
    "Major": [2, 2, 1, 2, 2, 2],
    "Natural Minor": [2, 1, 2, 2, 1, 2],
    "Harmonic Minor": [2, 1, 2, 2, 1, 3],
    "Melodic Minor": [2, 1, 2, 2, 2, 2],
    "Dorian Mode": [2, 1, 2, 2, 2, 1],
    "Mixolydian Mode": [2, 2, 1, 2, 2, 1],
    "Ahava Raba Mode": [1, 3, 1, 2, 1, 2],
    "Pentatonic Blues": [3, 2, 2, 3, 2]
}