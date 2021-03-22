import pyaudio
import wave
import numpy as np
import matplotlib.pyplot as plt

CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100

wf = wave.open(r'E:\毕设\代码\Project_sd1\LedZeppelin.wav','rb')
p = pyaudio.PyAudio()

stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
                channels=wf.getnchannels(),
                rate=wf.getframerate(),
                output=True)
data = wf.readframes(CHUNK)
print("Play the audio.\n")
while len(data) > 0:
    stream.write(data)
    data = wf.readframes(CHUNK)

stream.stop_stream()
stream.close()
p.terminate()


wf = wave.open('E:\毕设\代码\Project_sd1\LedZeppelin.wav','rb')
params = wf.getparams()
nchannels,sampwidth,framerate,nframes=params[:4]
str_data = wf.readframes(nframes)
wf.close()
wave_data = np.fromstring(str_data,dtype=np.short)
plt.figure()
plt.plot(wave_data)
plt.xlabel('Time(s)')
plt.ylabel("Amplitude")
plt.show()
