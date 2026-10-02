from gpiozero import PWMLED
from time import sleep


led = PWMLED(17)

try:
	# 1. 단계별 밝기 변경 (0.0 ~ 1.0)
	print("단계별 밝기 제어 시작")
	for value in [0.0, 0.25, 0.5, 0.75, 1.0]:
		led.value = value
		print(f"현재 Duty Ratio: {value:.2f}")
		sleep(1.5)

	# 2. pulse()를 활용한 숨쉬기(Fade In/Out) 효과
	print("Fade In/Out 효과 실행")
	led.pulse(fade_in_time=1.0, fade_out_time=1.0, n=3, background=False)
finally:
	led.close()