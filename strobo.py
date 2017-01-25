from __future__ import division
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(17,GPIO.OUT)
try:
	while True:
		for i in range(5,20):
			p = i/100
			GPIO.output(17, GPIO.HIGH)
			time.sleep(p)
			GPIO.output(17, GPIO.LOW)
			time.sleep(p)
		for i in reversed(range(5,20)):
                        p = i/100
                        GPIO.output(17, GPIO.HIGH)
                        time.sleep(p)
                        GPIO.output(17, GPIO.LOW)
                        time.sleep(p)


except KeyboardInterrupt:
	pass

GPIO.cleanup()
