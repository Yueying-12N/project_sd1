# Abstract
This project uses Python to realize the transition from rhythm to pitch, which is eventually presented to the user in a simple GUI. The project is inspired
by a video by a music theory enthusiast Adam Neely([see here](https://www.youtube.com/watch?v=_gCJHNBEdoc&t=213s)). He argues that, fast rhythms can be perceived as pitches, and harmony is just complex interlocking polyrhythm. This project uses Python and some packages and libraries to first generate a square wave signal, then define a function to play the signal like a rhythm, then speed it up by changing the frequency of the signal, use the GUI to let the user input the ratio of the polyrhythm and drag the slider to change the speed, and finally can perceive how the polyrhythm sounds like a harmony by speeding it up.

# Requirements
## Software Packages
* OS: Windows, iOS
* Languages: Python
* Dependancies: numpy, scipy, sounddevice, time, pyaudio,PySimpleGUI，wave

# Installation and Setup
1. Download and setup Python3
2. Download the libraries listed above
3. run the 'poly.py' file in cmd
4. read the introduction on the GUI interface and input the polyrhythm

# Architecture
The project is based entirely on Python programming and some supporting libraries, with no additional use of external hardware. The code is divided into five main sections, with short functions and a user-friendly GUI. To demonstrate the conversion from rhythm to pitch, the project starts by generating a signal, playing it back to achieve like a rhythm. The user can set the ratio of the polyrhythm and drag the slider to change the speed and finally hear the pitch.
## Notes
### 1. Import libraries
This project use scipy signal module and numpy to generate the square wave as the signal, and use sounddevice and time to play the signal as the beat, then use PySimpleGUI for user to set the polyrhythm they want and change the speed to obtain the pitch, finally use matplotlib.pyplot and wave to show the waveform and spectrogram, which can observe more directly how the rhythm equals to pitch.
```
import numpy as np
from scipy import signal as sg
import sounddevice as sd
import time
import PySimpleGUI as sgu
import pyaudio
import matplotlib.pyplot as plt
import wave
```
### 2. Define variables
This part is define variables and set some parameters and initial values.
```
start_idx = 0
samplerate = sd.query_devices(None, 'output')['default_samplerate']
CHUNK = 1024
CHANNELS = 1
# pps: pulses per second, or can be seen as frequency here
pps1 = 1  # the first beat's frequency
pps2 = 1  # the second beat's frequency
pps3 = 1  # the third beat's frequency
sgu.theme('BlueMono')   # set the color if GUI
```
### 3. Define functions
This function will be given to the OutputStream object and is called whenever the stream needs a new chunk of sound to play. Parameters of the sound are changed via global external global variables like frequency.(Be careful that need to declare the global variables pps1-pps3)
```
def steam_callback(outdata, frames, time, status):
    if status:
        print(status, file=sys.stderr)
    global start_idx
    t = (start_idx + np.arange(frames)) / samplerate
    t = t.reshape(-1, 1)
    global pps1,pps2,pps3
    # generate beats with input parameters and add them
    # due to the duty of square wave is 0.5, so the pps is divided by 2
    # (pps: pulses per second)
    outdata[:] = 0.2*(sg.square(2*np.pi*(pps1/2)*t, duty=0.5)
    +sg.square(2*np.pi*(pps2/2)*t,duty=0.5)
    +sg.square(2*np.pi*(pps3/2)*t,duty=0.5))
    start_idx += frames

# The stream object: play sounds by writing to outdata in stream_callback().
stream = sd.OutputStream(   device = None,
                            channels = 1,
                            callback = steam_callback,
                            samplerate = samplerate)
```
### 4. Set GUI
A GUI (graphical user interface) is a system of interactive visual components for computer software. A GUI displays objects that convey information, and represent actions that can be taken by the user. So here in this project, the GUI is to let user to input the parameters of polyrhythm, then click the 'Ratio' button to submit the value. And drag the slider to change the speed, also there are three buttons under the slider to start or stop the playing.
```
layout = [  [sgu.Text('Please input the polyrhythm parameters (integer, start from 1):')],
            [sgu.Text('for example: if you want a 3:4 polyrhythm, enter 3 and 4')],
            [sgu.Text('first beat')],
            [sgu.InputText()],
            [sgu.Text('second beat (if no, enter 1)')],
            [sgu.InputText()],
            [sgu.Text('third beat (if no, enter 1)')],
            [sgu.InputText()],
            [sgu.Submit('Ratio')],
            [sgu.Text('Variate the pulse rate')],
            [sgu.Slider(range=(1,250),
            orientation='h',
            size=(34,20),
            enable_events=True,
            key='slider_change')],
            [sgu.Button('Start'),
            sgu.Button('Stop'),
            sgu.Button('Close')]
            ]
```
### 5. Define conditions
While different conditions, there will be corresponding operations.
Firstly, after user input the parameters and click 'Ratio' button, the beats will be set and updated each time user modify the input.

The project support 3 beats for 3 chooses:
* 1 beat: set 3 beats with same parameters
* 2 beats: input one beat with 1, then the polyrhythm contains two beats
* 3 beats: input 3 different parameters, can get a more complex polyrhythm

Then user can drag the slider to change the speed directly, the range is 1-250, which is enough to demonstrate how rhythm turns to pitch.
Also there are 3 buttons under:
*  Start : start to play
*  Stop : stop playing
*  Close : quit the program and close the window

```
while True:
    event, values = window.read()
    if event == 'Close':
        break

    if event == 'Stop':
        print('stream stopped')
        stream.stop()

    if event == 'Start':
        print('stream started')
        stream.start()

    if event == 'Ratio':
        ratio1 = float(values[0])
        ratio2 = float(values[1])
        ratio3 = float(values[2])
        window['Ratio'].update()
        print('the ratios are',ratio1,',',ratio2,'and',ratio3)

    if event == 'slider_change':
        speed = values['slider_change']
        pps1 = speed*ratio1
        pps2 = speed*ratio2
        pps3 = speed*ratio3
        window['slider_change'].update()
        print('Beat per second(BPS) changed to',speed)
        stream.start()
```
