import pyaudio
import time
from playsound import playsound
from datetime import datetime
import wave

now = datetime.now()

current_time = now.strftime("%H:%M:%S")

print('Hi, please enter initials- ')
print("Current Time =", current_time)
ini=input()
options=['Left','Right','Forward','Backward','Left','Right','Up','Down','Stop','Select']
for i,option in enumerate(options):
    print('Recording number'+str(i))
    filename=str(ini)+'-'+ option +'-'+ current_time+'.wav'
    chunk = 1024
    FORMAT = pyaudio.paInt16
    channels = 1
    sample_rate = 44100
    record_seconds = 2
    p = pyaudio.PyAudio()
    stream = p.open(format=FORMAT,channels=channels,rate=sample_rate,input=True,output=True,frames_per_buffer=chunk)
    frames = []
    print('Say    * '+ option +' *      After the beep ends')
    time.sleep(1)
    playsound("beep-01a.wav")
    
    time.sleep(0.15)
    print("Recording...")
    for i in range(int(44100 / chunk * record_seconds)):
        data = stream.read(chunk,exception_on_overflow = False)
        
        # stream.write(data)
        frames.append(data)
    print('Recorded, press control c to quit. Wait 3 seconds then i will save')
    stream.stop_stream()
    stream.close()

    p.terminate()
    time.sleep(3)
    wf = wave.open(filename, "wb")
    wf.setnchannels(channels)
    wf.setsampwidth(p.get_sample_size(FORMAT))
    wf.setframerate(sample_rate)
    wf.writeframes(b"".join(frames))
    wf.close()
print('Session over.')
time.sleep(4)
