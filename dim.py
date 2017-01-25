import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)

GPIO.setup(17, GPIO.OUT)

dim = GPIO.PWM(17, 50)

dim.start(0)

try:

	while True:
		for i in range(100):
			dim.ChangeDutyCycle(i)
			time.sleep(0.005)
		for i in range(100):
			dim.ChangeDutyCycle(100-i)
			time.sleep(0.005)
except KeyboardInterrupt:
	pass

dim.stop()

GPIO.cleanup()

