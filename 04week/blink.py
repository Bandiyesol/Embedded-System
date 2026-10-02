from gpiozero import LED
from time import sleep


led = LED(17)

try:
	# 1. for 반복문을 통한 제어
	print("for문 기반 5회 점멸 시작")
	for i in range(5):
		led.on()
		sleep(1.0)
		led.off()
		sleep(1.0)
		print(f"점멸 횟수: {i+1}")

	sleep(1)

	# 2. gpiozero blink() 비동기 점멸 방식
	print("gpiozero blink() 비동기 점멸 시작")
	led.blink(on_time=0.2, off_time=0.8, n=5, background=False)
finally:
	led.close()