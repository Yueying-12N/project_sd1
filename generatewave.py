import numpy as np
from scipy import signal as sg
import matplotlib.pyplot as plt

freq = 2
amp = 2
time = np.linspace(0, 2, 1000)

'''sin wave'''
signal_sin = amp*np.sin(2*np.pi*freq*time)
plt.figure(1)
plt.plot(time, signal_sin)
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.show()


'''square wave'''
signal_square = amp*sg.square(2*np.pi*freq*time, duty=0.3)
plt.figure(2)
plt.plot(time,signal_square)
plt.xlabel('Time(s)')
plt.ylabel('Amplitude')
plt.show()

'''triangle wave'''
signal_tri = amp*sg.sawtooth(2*np.pi*freq*time, width=0.5)
plt.figure(3)
plt.plot(time,signal_tri)
plt.xlabel('Time(s)')
plt.ylabel('Amplitude')
plt.show()
