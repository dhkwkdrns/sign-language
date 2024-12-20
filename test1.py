import serial
from gtts import gTTS
import os
from playsound import playsound

# 아두이노와 연결된 시리얼 포트 설정 (아두이노 IDE에서 확인한 포트를 입력하세요)
arduino_port = "COM3"  # Windows의 경우 "COM3", macOS/Linux의 경우 "/dev/ttyUSB0"
baud_rate = 9600       # 아두이노와 동일한 보드레이트 설정
ser = serial.Serial(arduino_port, baud_rate)

print("아두이노와 연결 중...")

try:
    while True:
        # 시리얼 데이터가 도착하면 읽기
        if ser.in_waiting > 0:
            message = ser.readline().decode('utf-8').strip()  # 데이터 읽기 및 문자열로 변환
            print(f"받은 데이터: {message}")
            
            # GTTS를 사용해 음성 파일 생성
            tts = gTTS(text=message, lang='ko')  # lang='ko'는 한국어 설정
            tts.save("output.mp3")
            print("음성 파일 생성 완료!")

            # 음성 파일 재생
            playsound("output.mp3")
            print("음성 출력 완료!")

            # 사용 후 파일 삭제 (필요시 유지 가능)
            os.remove("output.mp3")

except KeyboardInterrupt:
    print("프로그램 종료")
    ser.close()
