# 패키지
## json 

## import_ipynb
ipynb 파일을 import하기 위해 사용
py 파일로 변환할 경우 필요 없음

## requests

## playsound

## scipy.io.wavfile


## picamera 
 사진 촬영

# 사용법
```python
import from APIs.get_emotion_by_text get_emotion_by_text
import from APIs.get_emotion_by_image get_emotion_by_image

result1 = get_emotion_by_text('안녕하세요')
result2 = get_emotion_by_image() #image file must be located in /APIs.
print(result1)
print(result2)
```
