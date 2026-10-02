from gpiozero import LED
from time import sleep


# BCM GPIO17 객체 생성
led = LED(17)

try:
	print("LED ON (2 seconds)")
	led.on()
	sleep(2)
	print("LED OFF")
	led.off()
finally:
	led.close()