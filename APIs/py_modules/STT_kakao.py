#!/usr/bin/env python
# coding: utf-8

# In[7]:


import requests
import json

def speech_to_text():
    kakao_speech_url = "https://kakaoi-newtone-openapi.kakao.com/v1/recognize"

    ##get key from  https://developers.kakao.com/product
    rest_api_key = '293253972858d4b09d46fc714d9de181' #한달 

    headers = {
        "Content-Type": "application/octet-stream",
        "X-DSS-Service": "DICTATION",
        "Authorization": "KakaoAK " + rest_api_key,
    }

    with open('audio_file.wav', 'rb') as af: 
        audio = af.read()

    result = requests.post(kakao_speech_url, headers=headers, data=audio)
    #print(result)
    print(result.text)




