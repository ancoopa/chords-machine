from pyo import *

class ChordsMachine:
  CHORD = {
    # 'maj7': [4, 7, 11],
    # 'm7': [3, 7, 10],
    # 'x7': [4, 7, 10],
    # 'half_dim': [3, 6, 10]
    'maj7': [-12, -8, -5, -1],
    'm7': [-12, -9, -5, -2],
    'x7': [-12, -8, -5, -2],
    'half_dim': [-12, -9, -6, -2]
  }

  def __init__(self):
    self.harm_1, self.harm_3, self.harm_5, self.harm_7 = None, None, None, None
    s = Server()

    # Inputs/Outputs may differ on your computer.
    s.setInputDevice(3)
    # s.setOutputDevice(3)
    s.setOutputDevice(5) # Headphones
    s.setMidiInputDevice(99) # Open all input devices.
    s.boot()

    self.mic = Input().play().out()
    self.notes = Notein(poly=10, scale=0, first=0, last=127, channel=0, mul=1)

    tfon = TrigFunc(self.notes["trigon"], self.handle_note_on, arg=list(range(10)))
    tfoff = TrigFunc(self.notes["trigoff"], self.handle_note_off, arg=list(range(10)))

    s.start()
    s.gui(locals())

  def chord(self, chordType, with_ui=False):
    tones = self.CHORD[chordType]
    self.harm_1 = Harmonizer(mic, transpo=tones[0]).out(1)
    self.harm_3 = Harmonizer(mic, transpo=tones[1]).out(1)
    self.harm_5 = Harmonizer(mic, transpo=tones[2]).out(1)
    self.harm_7 = Harmonizer(mic, transpo=tones[3]).out(1)
    if (with_ui):
      self.harm_1.ctrl(title="harm_1")
      self.harm_3.ctrl(title="harm_3")
      self.harm_5.ctrl(title="harm_5")
      self.harm_7.ctrl(title="harm_7")
      
  def chord_stop(self):
    self.harm_1.stop()
    self.harm_3.stop()
    self.harm_5.stop()
    self.harm_7.stop()
    print('No chords.')

  def handle_note_on(self, voice):
    pit = int(self.notes["pitch"].get(all=True)[voice])
    vel = int(self.notes["velocity"].get(all=True)[voice] * 127)
    self.switch_chords_stop(pit)

  def handle_note_off(self, voice):
    pit = int(self.notes["pitch"].get(all=True)[voice])
    vel = int(self.notes["velocity"].get(all=True)[voice] * 127)
    self.chord_stop()
  
  def switch_chords_stop(self, pit):
    if pit == 48:
      print('Chord: maj7')
      return self.chord('maj7')
    elif pit == 49:
      print('Chord: m7')
      return self.chord('m7')
    elif pit == 50:
      print('Chord: x7')
      return self.chord('x7')
    elif pit == 51:
      print('Chord: half_dim')
      return self.chord('half_dim')

ChordsMachine()
