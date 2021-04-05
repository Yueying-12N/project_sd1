#generate a square wave and play with def function_square_wave_sample

import numpy as np
from scipy import signal as sg
import pyaudio

CHUNK = 1024
CHANNELS = 1

#Open a stream with settings
p = pyaudio.PyAudio()
stream = p.open(format=pyaudio.paFloat32,
                rate=44100,  #standard samplerate
                channels= CHANNELS,
                frames_per_buffer=CHUNK,
                output=True,
                output_device_index=2
                )

#check the device index and the maximum of channals
#for i in range(p.get_device_count()):
#   dev = p.get_device_info_by_index(i)
#   print((i,dev['name'],dev['maxInputChannels']))

#outputs a waveform that is ready to be played
def square_wave_sample(duration, pps):
    sr = 22050     #a fixed samplerate
    T = duration
    t = np.linspace(0, T, int(T*sr), endpoint=False)
    samples = 0.5*sg.square(2*np.pi*pps*t,duty=0.5)
    stream.write(samples.astype(np.float32).tobytes())
    stream.close()

dur = input("please input the duration:")
pps = input("please input the pulses per second within 10 to 880:")

#as input() returns the string, translate the dtype
# due to the duration may be 0.5second so here duration use float
dur = float(dur)
pps = int(pps)
square_wave = square_wave_sample(dur,pps)
