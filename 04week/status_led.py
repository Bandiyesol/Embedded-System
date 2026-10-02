from gpiozero import LED
from time import sleep


led = LED(17)

def show_ok():
	"""정상 상태: 느린 깜빡임 (1s ON / 1s OFF)"""
	print("[State: OK] 시스템 정상 작동 중...")
	led.blink(on_time=1.0, off_time=1.0, n=3, background=False)

def show_warning():
	"""경고 상태: 빠른 깜빡임 (0.2s ON / 0.2s OFF)"""
	print("[State: WARNING] 주의가 필요함.")
	led.blink(on_time=0.2, off_time=0.2, n=3, background=False)

def show_error():
	"""오류 상태: 세번 짧은 깜빡임 후 긴 휴지"""
	print("[State: ERROR] 시스템 에러 발생!")
	for _ in range(2):
		for _ in range(3):
			led.on()
			sleep(0.1)
			led.off()
			sleep(0.1)
		sleep(1.5)

try:
	show_ok()
	show_warning()
	show_error()
finally:
	led.close()