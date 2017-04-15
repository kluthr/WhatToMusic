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
    "C5": 523.25,
    "C#5":554.37,
    "D5": 587.33,
    "D#5": 622.25,
    "E5": 659.25,
    "F5": 698.46,
    "F#5": 739.99,
    "G5": 783.99,
    "G#5": 830.61,
    "A5": 880.00,
#    "A#5":932.33,
#    "B5": 987.77,
#    "C6": 1046.50
    }

NAMES = list(FREQUENCIES)

BEATS = [1.0, 0.75, 0.5, 0.25, 0.125]

MEASURE = 1

SCALES = {
    "major": [2, 2, 1, 2, 2, 2],
    "natural minor": [2, 1, 2, 2, 1, 2],
    "harmonic minor": [2, 1, 2, 2, 1, 3],
    "melodic minor": [2, 1, 2, 2, 2, 2],
    "dorian mode": [2, 1, 2, 2, 2, 1],
    "mixolydian mode": [2, 2, 1, 2, 2, 1],
    "ahava raba mode": [1, 3, 1, 2, 1, 2],
    "pentatonic blues": [3, 2, 2, 3, 2]
}
