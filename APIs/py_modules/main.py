from playsound import PlaysoundException
import record_audio_data
import get_emotion_by_image
import get_emotion_by_text
import get_token
import read_config
import record_audio_data
import STT_kakao
import take_new_image
import TTS_lg
import time
import audioop
import pyaudio

import pygame
import time
import multiprocessing
import wave



if __name__ == '__main__' :
	#token
	#미러모지 확인
	CHUNK = 1024
	FORMAT = pyaudio.paInt16
	CHANNELS = 1
	RATE = 44100
	RECORD_SECONDS = 5
	WAVE_OUTPUT_FILENAME = "output.wav"

	while True:
		record_audio_data.record_for_seconds(3)
		speech_text = STT_kakao.speech_to_text()
		print(speech_text)
		if speech_text.find("미러") != -1 or speech_text.find("모지") != -1 or speech_text.find("뭐지") != -1 or speech_text.find('보지') != -1 or speech_text.find("이거") != -1:
			print("미러모지 감지")
			pygame.mixer.init()
			pygame.mixer.music.load('ok.mp3')
			pygame.mixer.music.play()

			record_audio_data.record_for_seconds(5)
			speech_text = STT_kakao.speech_to_text()

			if speech_text.find("감정") != -1:
				take_new_image.take_new_image()
				emotion = "현재 감정은 "+ get_emotion_by_image.get_emotion_by_image()+ "입니다."
				TTS_lg.text_to_speech(emotion)
				pygame.mixer.init()
				pygame.mixer.music.load('mp3_file.mp3')
				pygame.mixer.music.play()
				time.sleep(3)

