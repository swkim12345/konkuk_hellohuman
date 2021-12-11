#!/usr/bin/env python
# coding: utf-8

# In[3]:


import requests
import json
import time
from playsound import playsound
import import_ipynb
from read_config import *
from get_token import get_token

def text_to_speech(text):
  token = get_token()
  data_sample =json.dumps({
    "type": "SYNTHESIS",
    "input": {
      "text": text,
      "type": "Plain Text"
    },
    "voiceConfig": {
      "speaker": "Female1",
      "speed": "Medium",
      "languageCode": "ko_KR",
      "effect": "None",
      "volume": "Volume 4",
      "pitch": "Normal"
    },
    "audioConfig": {
      "encoding": "MP3"
    },
    "additionalConfig": {
      "privacy": "yes"
    }
  }, sort_keys=False)

  rest_api_key = read_rest_api_key()
  headers = {
      "Content-Type": 'application/json',
      "x-api-key": rest_api_key,
      "Authorization": token
  }
  URL = 'https://korea.api.lgthinqai.net:443/voice/tts/v1/synthesis'
  voice_parse = requests.post(URL, headers = headers, data=data_sample)

  mp3_file = voice_parse.content

  with open("mp3_file.mp3", "wb") as f:
      f.write(mp3_file)




