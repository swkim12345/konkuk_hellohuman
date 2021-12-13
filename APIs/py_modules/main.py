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
			ok = "네"
			TTS_lg.text_to_speech(ok)
			pygame.mixer.init()
			pygame.mixer.music.load('mp3_file.mp3')
			pygame.mixer.music.play()

			record_audio_data.record_for_seconds(5)
			speech_text = STT_kakao.speech_to_text()

			if speech_text.find("감정") != -1:
				screenWatch = "카메라를 봐주세요."
				TTS_lg.text_to_speech(screenWatch)
				pygame.mixer.init()
				pygame.mixer.music.load('mp3_file.mp3')
				pygame.mixer.music.play()

				take_new_image.take_new_image()
				newEmotion = get_emotion_by_image.get_emotion_by_image()
				emotion = "현재 감정은 "+ newEmotion+ "입니다."
				TTS_lg.text_to_speech(emotion)
				pygame.mixer.init()
				pygame.mixer.music.load('mp3_file.mp3')
				pygame.mixer.music.play()
				if newEmotion == "슬픔" :
					emotion = "저녁은 치킨이 맛있지 않을까요? 배고파요..."
					TTS_lg.text_to_speech(emotion)
					pygame.mixer.init()
					pygame.mixer.music.load('mp3_file.mp3')
					pygame.mixer.music.play()
				time.sleep(3)

			elif speech_text.find("시간") != -1:
				tm = time.localtime(time.time())
				timeSpeech = "현재 시간은 " + str(tm.tm_hour) + "시, " + str(tm.tm_min) + "분 입니다."
				TTS_lg.text_to_speech(timeSpeech)
				pygame.mixer.init()
				pygame.mixer.music.load('mp3_file.mp3')
				pygame.mixer.music.play()
				time.sleep(3)

			elif speech_text.find("잘") != -1 or speech_text.find("자") != -1 :
				sleepSpeech = "좋은 밤 되세요."
				TTS_lg.text_to_speech(sleepSpeech)
				pygame.mixer.init()
				pygame.mixer.music.load('mp3_file.mp3')
				pygame.mixer.music.play()
				time.sleep(3)

			else :
				notSpeech = "다시 말씀해 주세요"
				TTS_lg.text_to_speech(notSpeech)
				pygame.mixer.init()
				pygame.mixer.music.load('mp3_file.mp3')
				pygame.mixer.music.play()
				time.sleep(3)

