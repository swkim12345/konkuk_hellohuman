#!/usr/bin/env python
# coding: utf-8

# In[18]:



### THIS FILE IS LEGACY.
### USE "get_emotion_by_text.ipynb"

import requests
import json
import base64
import requests
from requests_toolbelt.multipart.encoder import MultipartEncoder
client_ID = '2q9q3l4gi3lr0nuad91runfaqf'
client_PW = '1rrj3nk1u3rkoten4k3n60t397mliimt6p8dqibr7o4ifole8ocn'
auth_raw = client_ID + ':' + client_PW
auth_byte = auth_raw.encode('ascii')
auth_base64 = base64.b64encode(auth_byte)
auth = 'Basic ' + auth_base64.decode('ascii')
r = requests.post('https://oauth.api.lgthinqai.net:443/v1/cognito/', headers={'Authorization' : auth, 'Content-Type' : 'application/x-www-form-urlencoded'})

token = r.json()["access_token"]
emotion_recognition_url = "https://korea.api.lgthinqai.net:443/emotion/er/v1/recognition"
rest_api_key = 'MTtlYjQ1Zjk5ZTVjMDU0ZTRmODJhOTEzN2JkZGJjZDAxNzsxNjM2NjAxMTY4OTEz'

headers = {
    "Content-Type": 'multipart/form-data;charset=UTF-8',
    "x-api-key": rest_api_key,
    "Authorization": token
}

mp_encoder = MultipartEncoder(
    fields={        'Authorization': 'hell',
        'Content-Type': 'multipart/form-data;charset=UTF-8',
        'x-api-key': "hello",
        'config': 'hello',
        
        'type': 'EMOTION_RECOGNITION',
        'input': '{ \
            "type": "TEXT", \
            "text": "나는 지금 매우 화가 나 있습니다."\
        }'
    }
)
body = {
    "type": "EMOTION_RECOGNITION",
    "input": { 
        "type": "TEXT", 
        "text": "나는 지금 매우 화가 나 있습니다."
    },
    "config": "TEXT"
}
#text = "hello"
#b_txt = text.encode('utf-8')
#files = dict(config="------12345")

#res = requests.post(emotion_recognition_url, headers = headers, data = body, files = {"config":"hello"})
print(mp_encoder)

r = requests.post(
    emotion_recognition_url,
    data=mp_encoder,  
    headers={'Content-Type': 'multipart/form-data;charset=UTF-8', 'x-api-key': rest_api_key, 'Authorization': token})
print(r.text)
print(r)


# In[ ]:





# In[ ]:




