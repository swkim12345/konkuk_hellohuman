#!/usr/bin/env python
# coding: utf-8

# In[20]:


import base64
import requests
import import_ipynb
from read_config import *

def get_token():
    client_ID = read_client_ID()
    client_PW = read_client_PW()
    auth_URL = read_auth_URL()

    auth_raw = client_ID + ':' + client_PW
    auth_byte = auth_raw.encode('ascii')
    auth_base64 = base64.b64encode(auth_byte)
    auth = 'Basic ' + auth_base64.decode('ascii')


    r = requests.post(auth_URL, headers={'Authorization' : auth, 'Content-Type' : 'application/x-www-form-urlencoded'})
    token = r.json()["access_token"]
    #print(token)
    return token


# In[ ]:




