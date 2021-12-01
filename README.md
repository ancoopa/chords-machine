# About
The repository is created as a follow up for the YouTube micro-series:    
Ep.1: https://youtu.be/MhOyVMbLbvw    
Ep.2: https://youtu.be/0wf1yLVWV4o    
    
Tested on MacOS "Big Sur" only.    
Python 3.8 is required.

# Installation
Install following libraries first:
```
brew install portaudio
brew install libsndfile
brew install portmidi
brew install liblo
```

And if you need GUI:
```
pip install -U wxPython==4.1.0
```

Then install the main library:
```
pip install -U pyo
```

## System settings
In order for `pyo` to be able to access speakers, microphones, allow audio to the terminal app in the MacOS settings:        
```
Security & Privacy => Microphone => [v] Terminal
```
## How to run
The main file to run is named `chord_machine.py`.