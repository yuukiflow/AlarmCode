import pigpio
import time

#pin 17 = rouge
#pin 22 = vert
#pin 24 = bleu

RED_PIN = 17
GREEN_PIN = 22
BLUE_PIN = 24

try:

	pi = pigpio.pi()

	while True:
		for i in range(2, 255):
			pi.set_PWM_dutycycle(RED_PIN, i)
			pi.set_PWM_dutycycle(BLUE_PIN, i)
			pi.set_PWM_dutycycle(GREEN_PIN, i)
			time.sleep(7)

		pi.set_PWM_dutycycle(RED_PIN, 255)
		pi.set_PWM_dutycycle(BLUE_PIN, 255)
                pi.set_PWM_dutycycle(GREEN_PIN, 255)

	    
except KeyboardInterrupt:
    pass

pi.set_PWM_dutycycle(RED_PIN, 0)
pi.set_PWM_dutycycle(BLUE_PIN, 0)
pi.set_PWM_dutycycle(GREEN_PIN, 0)

pi.stop()
