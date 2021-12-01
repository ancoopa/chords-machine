from pyo import *

CHORD = {
  'maj7': [-12, -8, -5, -1],
  'm7': [-12, -9, -5, -2],
  'x7': [-12, -8, -5, -2],
  'half_dim': [-12, -9, -6, -2]
}

s = Server()

s.setInputDevice(3) # Steinberg in
s.setOutputDevice(3) # Steinberg out
s.setMidiInputDevice(99)
s.boot()

mic = Input().play().out()
notes = Notein(poly=10, scale=0, first=0, last=127, channel=0, mul=1)

harm_1, harm_3, harm_5, harm_7 = None, None, None, None

def chord(chordType):
  global mic, CHORD, harm_1, harm_3, harm_5, harm_7
  tones = CHORD[chordType]
  harm_1 = Harmonizer(mic, transpo=tones[0]).out()
  harm_3 = Harmonizer(mic, transpo=tones[1]).out()
  harm_5 = Harmonizer(mic, transpo=tones[2]).out()
  harm_7 = Harmonizer(mic, transpo=tones[3]).out()

def handle_note_on(voice):
  pit = int(notes["pitch"].get(all=True)[voice])
  if pit == 48:
    chord('maj7')
    print('Chord: maj7')
  elif pit == 49:
    chord('m7')
    print('Chord: m7')
  elif pit == 50:
    chord('x7')
    print('Chord: x7')
  elif pit == 51:
    chord('half_dim')
    print('Chord: half_dim')

def handle_note_off(voice):
  global harm_1, harm_3, harm_5, harm_7
  harm_1.stop()
  harm_3.stop()
  harm_5.stop()
  harm_7.stop()
  print('No chords.')

tfon = TrigFunc(notes["trigon"], handle_note_on, arg=list(range(10)))
tfoff = TrigFunc(notes["trigoff"], handle_note_off, arg=list(range(10)))

s.start()
s.gui(locals())
