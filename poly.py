#old version only support 2 beats with inconvenient input

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
pps2 = pps1*ratio
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
    global pps1,ratio,pps2
    # mix two beats
    outdata[:] = 0.2*(sg.square(2*np.pi*(pps1/2)*t, duty=0.5)
    +sg.square(2*np.pi*(pps2/2)*t,duty=0.5))
    start_idx += frames

# The stream object: play sounds by writing to outdata in stream_callback().
stream = sd.OutputStream(   device = None,
                            channels = 1,
                            callback = steam_callback,
                            samplerate = samplerate)

# All the stuff inside window.
layout = [  [sgu.Text('Please input the ratio of two beats(support decimal):')],
            [sgu.Text('Hints:for example, if you want 3/4 Polyrhythm,the ratio is 4/3=1.333')],
            [sgu.Text('(useful decimal: 1/3=0.333,1/6=0.167,1/7=0.143)')],
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
        ratio = float(values[0])
        window['Ratio'].update()
        print('the ratio is ',ratio)

    if event == 'slider_change':
        pps1 = values['slider_change']
        pps2 = pps1*ratio
        window['slider_change'].update()
        print('basic BPM changed to',pps1)
        stream.start()

window.close()
