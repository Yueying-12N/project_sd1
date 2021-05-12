import numpy as np
from scipy import signal as sg
import sounddevice as sd
import time
import PySimpleGUI as sgu
import pyaudio
import matplotlib.pyplot as plt
import wave

start_idx = 0  #freqs = np.arange(1,5,0.1);#frequency = freqs[0];
samplerate = sd.query_devices(None, 'output')['default_samplerate']
CHUNK = 1024
CHANNELS = 1
ratio = 1
pps1 = 1
pps2 = 1
pps3 = 1
sgu.theme('BlueMono')   # Add a touch of color

# This function will be given to the OutputStream object and is called whenever
# the stream needs a new chunk of sound to play. Parameters of the sound are
# changed via global external (global) variables (like frequency, in this case).
def steam_callback(outdata, frames, time, status):
    if status:
        print(status, file=sys.stderr)
    global start_idx
    t = (start_idx + np.arange(frames)) / samplerate
    t = t.reshape(-1, 1)
    global pps1,ratio,pps2,pps3
    # mix two beats
    outdata[:] = 0.2*(sg.square(2*np.pi*(pps1/2)*t, duty=0.5)
    +sg.square(2*np.pi*(pps2/2)*t,duty=0.5)
    +sg.square(2*np.pi*(pps3/2)*t,duty=0.5))
    start_idx += frames

# The stream object: play sounds by writing to outdata in stream_callback().
stream = sd.OutputStream(   device = None,
                            channels = 1,
                            callback = steam_callback,
                            samplerate = samplerate)

# All the stuff inside window.
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
window = sgu.Window('Polyrhythm', layout)

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
        print('basic BPM changed to',speed)
        stream.start()

window.close()
