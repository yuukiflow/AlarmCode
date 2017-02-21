import RPi.GPIO as GPIO
import time
import pigpio

GPIO.setmode(GPIO.BCM)

GPIO.setup(13, GPIO.IN, pull_up_down=GPIO.PUD_UP)

RED_PIN = 17
GREEN_PIN = 22
BLUE_PIN = 24

pi = pigpio.pi()

global Brightness
global LightOn
global Push
global ButtonPressed

LightOn = False
push = False
ButtonPressed = False
Brightness = 0

try:
	while True:
		print('stage 1')
		push = GPIO.input(13)
		time.sleep(0.1)
		if push == False & LightOn == False:
			print('stage 2')
			ButtonPressed = True
			LightOn = True
			Brightness = 255
			time.sleep(0.1)
		elif push == False & LightOn == True:
			print('stage3')
			ButtonPressed = False
			LightOn = False
			Brightness = 0
			time.sleep(0.1)
		if LightOn == True:
			print('stage 4')
			pi.set_PWM_dutycycle(RED_PIN, Brightness)
  			pi.set_PWM_dutycycle(BLUE_PIN, Brightness)
                        pi.set_PWM_dutycycle(GREEN_PIN, Brightness)
			time.sleep(0.1)
		elif LightOn == False:
			print('stage 5')
			pi.set_PWM_dutycycle(RED_PIN, Brightness)
  			pi.set_PWM_dutycycle(BLUE_PIN, Brightness)
                        pi.set_PWM_dutycycle(GREEN_PIN, Brightness)
			time.sleep(0.1)

except KeyboardInterrupt:
	pass

pi.set_PWM_dutycycle(RED_PIN, 0)
pi.set_PWM_dutycycle(BLUE_PIN, 0)
pi.set_PWM_dutycycle(GREEN_PIN, 0)


pi.stop()

GPIO.cleanup()
