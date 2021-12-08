#!/usr/bin/env python
# coding: utf-8

# In[2]:


import queue, os, threading
import sounddevice as sd
import soundfile as sf
from scipy.io.wavfile import write
import time

import requests
import json

q = queue.Queue()
recorder = False
recording = False

def complicated_record():
    with sf.SoundFile("audio_file.wav", mode='w', samplerate=16000, subtype='PCM_16', channels=1) as file:
        with sd.InputStream(samplerate=16000, dtype='int16', channels=1, callback=complicated_save):
            while recording:
                file.write(q.get())
        
def complicated_save(indata, frames, time, status):
    q.put(indata.copy())
    
def start_recording():
    global recorder
    global recording
    recording = True
    recorder = threading.Thread(target=complicated_record)
    print('start recording')
    recorder.start()
    
def stop_recording():
    global recorder
    global recording
    recording = False
    recorder.join()
    print('stop recording')
    
def record_for_seconds(seconds):
    start_recording()
    time.sleep(5)
    stop_recording()
    






