import serial
from gtts import gTTS
import os
import threading
from playsound import playsound

# COM3 포트 설정
ser = serial.Serial('COM3', 9600)

# 이전 요청 저장 변수
last_request = None

def play_tts(request_text):
    # TTS 생성 및 재생
    tts = gTTS(text=request_text, lang='ko')
    filename = "output.mp3"
    tts.save(filename)

    print(f"TTS 재생 중: {request_text}")
    playsound(filename)

    # MP3 파일 삭제
    os.remove(filename)

def handle_request():
    global last_request
    while True:
        if ser.in_waiting > 0:  # 시리얼 데이터가 있으면 읽기
            incoming_data = ser.readline().decode('utf-8').strip()
            print(f"받은 요청: {incoming_data}")

            # 이전 요청과 다를 경우에만 처리
            if incoming_data != last_request:
                last_request = incoming_data

                # 새로운 요청을 처리하는 스레드 생성
                tts_thread = threading.Thread(target=play_tts, args=(incoming_data,))
                tts_thread.start()

try:
    handle_request()

except KeyboardInterrupt:
    print("프로그램 종료")
    ser.close()