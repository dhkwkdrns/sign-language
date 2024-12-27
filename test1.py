import serial
import time
from gtts import gTTS
import os

# 아두이노와 연결할 시리얼 포트 설정 (시리얼 포트와 보드 속도에 맞게 변경)
arduino_port = 'COM3'  # 예시로 리눅스에서 사용되는 포트 (Windows는 COM 포트 예: COM3)
baud_rate = 9600

# 시리얼 포트 열기
ser = serial.Serial(arduino_port, baud_rate)
time.sleep(2)  # 아두이노가 초기화 될 때까지 대기

# 시리얼 데이터 읽고 TTS로 출력하는 루프
try:
    while True:
        if ser.in_waiting > 0:
            # 아두이노에서 받은 텍스트 읽기
            arduino_input = ser.readline().decode('utf-8').strip()  # 아두이노에서 보내는 텍스트
            
            # 텍스트가 비어있지 않으면 TTS로 출력
            if arduino_input:
                print(f"Received from Arduino: {arduino_input}")
                
                # gTTS를 사용해 음성으로 변환
                tts = gTTS(text=arduino_input, lang='ko')  # 한국어로 출력
                tts.save("output.mp3")  # 음성 파일 저장
                
                # 음성 파일 재생 (Windows에서는 다른 방법으로 플레이할 수도 있음)
                os.system("start output.mp3")  # Windows에서 mp3 파일을 실행
                # os.system("mpg321 output.mp3")  # Linux에서 mpg321으로 음성 파일 재생
                time.sleep(1)  # 잠시 대기하여 음성 파일이 재생되는 동안 기다리기
except KeyboardInterrupt:
    print("프로그램 종료")
    ser.close()
