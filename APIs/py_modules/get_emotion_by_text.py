#!/usr/bin/env python
# coding: utf-8

# In[4]:


import requests
import json
import base64
import import_ipynb

from read_config import *
from get_token import get_token

def get_emotion_by_text(text):
    token = str(get_token())
    emotion_recognition_url = "https://korea.api.lgthinqai.net:443/emotion/er/v1/recognition"
    rest_api_key = read_rest_api_key()

    headers = {
    #    "Content-Type": 'multipart/form-data;charset=UTF-8',   # 1. Content-Type 헤더 설정 삭제 (boundary 값을 라이브러리가 삽입해야 함)
        "x-api-key": rest_api_key,
        "Authorization": token
    }
    body = json.dumps({
        "type": "EMOTION_RECOGNITION",
        "input": { 
            "type": 'text', 
            "text": text 
        }
    }, ensure_ascii=False)   # 2. 삭제된 Content-Type의 UTF-8 대신 직접 UTF-8 보장 (필수 아님)

    # 정상 요청
    # {'x-api-key': 'MTtlYjQ1Zjk5ZTVjMDU0ZTRmODJhOTEzN2JkZGJjZDAxNzsxNjM2NjAxMTY4OTEz', 'Authorization': 'eyJraWQiOiJCeTd2YzJLa2c4Zkt3K2V0SFBwa1NlTVJUS0FmRWZWXC9NcGdmSmV3Nlo1QT0iLCJhbGciOiJSUzI1NiJ9.eyJzdWIiOiIycTlxM2w0Z2kzbHIwbnVhZDkxcnVuZmFxZiIsInRva2VuX3VzZSI6ImFjY2VzcyIsInNjb3BlIjoicmVzb3VyY2VfYWNjZXNzX3Njb3BlX2lkZW50aWZpZXJcL3N0dCByZXNvdXJjZV9hY2Nlc3Nfc2NvcGVfaWRlbnRpZmllclwvdHRzIHJlc291cmNlX2FjY2Vzc19zY29wZV9pZGVudGlmaWVyXC9ubHAgcmVzb3VyY2VfYWNjZXNzX3Njb3BlX2lkZW50aWZpZXJcL2VyIHJlc291cmNlX2FjY2Vzc19zY29wZV9pZGVudGlmaWVyXC9jcnVkIiwiYXV0aF90aW1lIjoxNjM3NjUyNDgxLCJpc3MiOiJodHRwczpcL1wvY29nbml0by1pZHAuYXAtbm9ydGhlYXN0LTIuYW1hem9uYXdzLmNvbVwvYXAtbm9ydGhlYXN0LTJfN1VUYXhzSVlzIiwiZXhwIjoxNjM3NjU2MDgxLCJpYXQiOjE2Mzc2NTI0ODEsInZlcnNpb24iOjIsImp0aSI6IjJiNGUzNDk5LWI0MDItNDViNi1iZTcwLTgwMzkwY2EyZGRkYSIsImNsaWVudF9pZCI6IjJxOXEzbDRnaTNscjBudWFkOTFydW5mYXFmIn0.WXBwVRXfDX7icNXlTCm72TeXth3-5jiKpykpksqJYZCW-7GwcgPSLp9oa3L1xK7driBSOuRMXatqcLRX-4qWPLdZU0bFCG0LU4TWepszfeYN9GxpfHhg2cPjmvx2Hx2F63KsqlL4D15qlaySzvPdWi5chxdv0SPKjxz48IpvXDttBEGy3gRwPhaw1uKE3420mDWoTelLeyO0x-gP7aFBGsqbPntgSBvW5uWUp8tX-RO9MLQ_e4f6IIH1pt-lIpN4vuIxYsZ0TI9TVr-CGTtav6Q2177K7zXsa1iGreOBEVeMyZTy8IXI7r0szCtTKp1krVai0GQx-qxw-ojysCHK6g', 'Content-Length': '240', 'Content-Type': 'multipart/form-data; boundary=c417d130bae7bef1fa8d1d70ebe844be'}
    # Content-Type 헤더 추가시 오류
    # {'Content-Type': 'multipart/form-data;charset=UTF-8', 'x-api-key': 'MTtlYjQ1Zjk5ZTVjMDU0ZTRmODJhOTEzN2JkZGJjZDAxNzsxNjM2NjAxMTY4OTEz', 'Authorization': 'eyJraWQiOiJCeTd2YzJLa2c4Zkt3K2V0SFBwa1NlTVJUS0FmRWZWXC9NcGdmSmV3Nlo1QT0iLCJhbGciOiJSUzI1NiJ9.eyJzdWIiOiIycTlxM2w0Z2kzbHIwbnVhZDkxcnVuZmFxZiIsInRva2VuX3VzZSI6ImFjY2VzcyIsInNjb3BlIjoicmVzb3VyY2VfYWNjZXNzX3Njb3BlX2lkZW50aWZpZXJcL3N0dCByZXNvdXJjZV9hY2Nlc3Nfc2NvcGVfaWRlbnRpZmllclwvdHRzIHJlc291cmNlX2FjY2Vzc19zY29wZV9pZGVudGlmaWVyXC9ubHAgcmVzb3VyY2VfYWNjZXNzX3Njb3BlX2lkZW50aWZpZXJcL2VyIHJlc291cmNlX2FjY2Vzc19zY29wZV9pZGVudGlmaWVyXC9jcnVkIiwiYXV0aF90aW1lIjoxNjM3NjUyNDU5LCJpc3MiOiJodHRwczpcL1wvY29nbml0by1pZHAuYXAtbm9ydGhlYXN0LTIuYW1hem9uYXdzLmNvbVwvYXAtbm9ydGhlYXN0LTJfN1VUYXhzSVlzIiwiZXhwIjoxNjM3NjU2MDU5LCJpYXQiOjE2Mzc2NTI0NTksInZlcnNpb24iOjIsImp0aSI6ImZiZDJlZDVlLTI5YmYtNDljOC1hYTc5LTViZjAwZTUwMTM0ZCIsImNsaWVudF9pZCI6IjJxOXEzbDRnaTNscjBudWFkOTFydW5mYXFmIn0.XbpqUUeLSBQ3GAnR7rnYjvqs0TrJV9gN6lneDm7akV6tVnw8fVXpLyuOqTiAfuQitZB8_7VGfzHUwvHamdmxYAlUCby0wg45MpbydWP8lWnwSqX58UB1GUWAO43ts5pRkFMMV9ZXxnZIkEu3wXiNhwr990ZO7m32CxphTWKKZywcSdUFL0Ec_EA0-bFkxN3aRhpg_vp2G0wImtThQOw3zNbCVIYThAY0sQ6S_jkYBeHSxzuBIGADVU0Xq0MY8_ZBUG_GdalmV4YMWAiLq2qArdMB5_vwigS-PP87StEFT0UtFTBKuCVNYvY7557LZfabwb5SZMi3x6NQICWGc9lBhg', 'Content-Length': '240'}

    res = requests.post(emotion_recognition_url, headers = headers, files = {"config" : (None, body)}) # 3. (data -> files 로 전환하고 filename 포함되지 않도록 튜플 첫번째 값 None 으로 설정)
    # print(requests.Request('POST', emotion_recognition_url, headers = headers, files = {"config" : (None, body)}).prepare().headers)
    # print(requests.Request('POST', emotion_recognition_url, headers = headers, files = {"config" : (None, body)}).prepare().body)

    print(res.json()['results']['uni_modal']['text']['result'])
    return (res.json()['results']['uni_modal']['text']['result'])



