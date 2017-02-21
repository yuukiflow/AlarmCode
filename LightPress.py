import RPi.GPIO as GPIO
import time
import pigpio

GPIO.setmode(GPIO.BCM)

GPIO.setup(13, GPIO.IN, pull_up_down=GPIO.PUD_UP)

RED_PIN = 17
GREEN_PIN = 22
BLUE_PIN = 24

pi = pigpio.pi()

State = -1
#LightOn = 0

try:
        while True:
		Push = GPIO.input(13)
		if Push == False:
			State = State * -1
			if State == 1:
                        	pi.set_PWM_dutycycle(RED_PIN, 255)
                        	pi.set_PWM_dutycycle(BLUE_PIN, 255)
                        	pi.set_PWM_dutycycle(GREEN_PIN, 255)
                        	#LightOn = 1
                        	time.sleep(0.5)
			if State == -1:
				pi.set_PWM_dutycycle(RED_PIN, 0)
                	        pi.set_PWM_dutycycle(BLUE_PIN, 0)
                	        pi.set_PWM_dutycycle(GREEN_PIN, 0)
				#LightOn = 0 
                	        time.sleep(0.5)

except KeyboardInterrupt:
        pass

pi.set_PWM_dutycycle(RED_PIN, 0)
pi.set_PWM_dutycycle(BLUE_PIN, 0)
pi.set_PWM_dutycycle(GREEN_PIN, 0)

pi.stop()

GPIO.cleanup()
