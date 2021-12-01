Tested on MacOS "Big Sur" only.    
Python 3.8 is required.

You should install following libraries first:
```
brew install portaudio
brew install libsndfile
brew install portmidi
brew install liblo
```

And if you need gui:
```
pip install -U wxPython==4.1.0
```

then:
```
pip install -U pyo
```


To allow the pyo to use speakers, microphones etc, allow audio to the terminal app in the OS settings:    
    
```
Security & Privacy => Microphone => [v] Terminal
```
