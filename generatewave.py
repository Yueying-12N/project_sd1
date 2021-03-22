import numpy as np
from scipy import signal as sg
import matplotlib.pyplot as plt

freq = 2
amp = 2
time = np.linspace(0, 2, 1000)
plt.figure(1)

'''sin wave'''
signal_sin = amp*np.sin(2*np.pi*freq*time)
plt.subplot(2,2,1)
plt.plot(time, signal_sin)
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')


'''square wave'''
signal_square = amp*sg.square(2*np.pi*freq*time, duty=0.3)
plt.subplot(2,2,2)
plt.plot(time,signal_square)
plt.xlabel('Time(s)')
plt.ylabel('Amplitude')


'''triangle wave'''
signal_tri = amp*sg.sawtooth(2*np.pi*freq*time, width=0.5)
plt.subplot(2,2,3)
plt.plot(time,signal_tri)
plt.xlabel('Time(s)')
plt.ylabel('Amplitude')
plt.show()


'''A pulse-width modulated sine wave'''
t = np.linspace(0, 1, 500, endpoint=False)
#plt.plot(t, sg.square(2 * np.pi * 5 * t))
#plt.ylim(-2, 2)
plt.figure(2)
sig = np.sin(2 * np.pi * t)
pwm = sg.square(2 * np.pi * 30 * t, duty=(sig + 1)/2)
plt.subplot(2, 1, 1)
plt.plot(t, sig)
plt.subplot(2, 1, 2)
plt.plot(t, pwm)
plt.ylim(-1.5, 1.5)
plt.show()
