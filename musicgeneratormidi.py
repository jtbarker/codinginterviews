from EasyMIDI import EasyMIDI,Track,Note,Chord,RomanChord
from random import choice

easyMIDI = EasyMIDI()
track1 = Track("acoustic grand piano")  # oops

c = Note('C', octave = 5, duration = 1/4, volume = 100)
e = Note('E', 5)
g = Note('G', 5)
chord = Chord([c,e,g])  # a chord of notes C, E and G
track1.addNotes([c, e, g, chord])

# roman numeral chord, first inversion (defaults to key of C)
track1.addNotes(RomanChord('I*', octave = 5, duration = 1))

easyMIDI.addTrack(track1)
easyMIDI.writeMIDI("output.mid")

