from gtts import gTTS
from playsound import playsound
import os

# 변환할 텍스트 입력
text = "안녕하세요, 이 텍스트는 음성으로 변환됩니다."

# GTTS 객체 생성 (언어는 한국어로 설정: lang='ko')
tts = gTTS(text=text, lang='ko')

# 음성 파일 저장
tts.save("output.mp3")
print("음성 파일 생성 완료!")

# 음성 파일 재생
playsound("output.mp3")
print("음성 출력 완료!")

# 사용 후 파일 삭제
os.remove("output.mp3")

print("aaa")