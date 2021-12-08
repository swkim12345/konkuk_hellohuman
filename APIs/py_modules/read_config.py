#!/usr/bin/env python
# coding: utf-8

# In[11]:


import json
from pprint import *
file_path = "config.json"
with open(file_path, "r") as json_file:
    json_data = json.load(json_file)

def read_client_ID():
    return json_data['client_ID']

def read_client_PW():
    return json_data['client_PW']

def read_rest_api_key():
    return json_data['rest_api_key']

def read_auth_URL():
    return json_data['auth_URL']

def read_all_data():
    return json_data

pprint(read_all_data())





