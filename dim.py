import RPi.GPIO as GPIO
import time
import pigpio

GPIO.setmode(GPIO.BCM)

GPIO.setup(13, GPIO.IN, pull_up_down=GPIO.PUD_UP)

RED_PIN = 17
GREEN_PIN = 22
BLUE_PIN = 24

pi = pigpio.pi()

global brightness
global LightState
global push

brightness = 0
LightState = False
push = GPIO.input(13)

try:

	while True:
		if push == True & LightState == False:
  			pi.set_PWM_dutycycle(RED_PIN, brightness)
  			pi.set_PWM_dutycycle(BLUE_PIN, brightness)
                        pi.set_PWM_dutycycle(GREEN_PIN, brightness)
			brightness = 255
			LightState = True
                        time.sleep(1)

		elif push == True & LightState == True:
                        pi.set_PWM_dutycycle(RED_PIN, brightness)
                        pi.set_PWM_dutycycle(BLUE_PIN, brightness)
                        pi.set_PWM_dutycycle(GREEN_PIN, brightness)
			brightness = 0
			LightState = False
                        time.sleep(1)
		time.sleep(0.1)


except KeyboardInterrupt:
	pass

pi.set_PWM_dutycycle(RED_PIN, 0)
pi.set_PWM_dutycycle(BLUE_PIN, 0)
pi.set_PWM_dutycycle(GREEN_PIN, 0)


pi.stop()

GPIO.cleanup()

