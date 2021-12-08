#!/usr/bin/env python
# coding: utf-8

# In[4]:


import numpy as np
import cv2
import time
start = time.time()  # 시작 시간 저장
 


# In[6]:


start = time.time()  # 시작 시간 저장
cap = cv2.VideoCapture(0) # 노트북 웹캠을 카메라로 사용
cap.set(3,1280) # 너비
cap.set(4,720) # 높이

ret, frame = cap.read() # 사진 촬영

cv2.imwrite('self camera test.jpg', frame) # 사진 저장
    
cap.release()
cv2.destroyAllWindows()
print("time :", time.time() - start)  # 현재시각 - 시작시간 = 실행 시간


# In[7]:


from picamera import PiCamera
from time import sleep

camera = PiCamera()

camera.start_preview()
sleep(5)
camera.capture('camera_test.jpg')
camera.stop_preview()


# In[ ]:




