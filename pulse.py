import RPi.GPIO as GPIO
import time
import pigpio

pi = pigpio.pi()


try:

        while True:
            for i in range(2, 255):
		pi.set_PWM_dutycycle(17, i)
		pi.set_PWM_dutycycle(22, i)
		pi.set_PWM_dutycycle(24, i)
		time.sleep(0.005)

	    for i in range(2, 255):
                pi.set_PWM_dutycycle(17, 255-i)
                pi.set_PWM_dutycycle(22, 255-i)
                pi.set_PWM_dutycycle(24, 255-i)
                time.sleep(0.005)


except KeyboardInterrupt:
    pass

pi.set_PWM_dutycycle(17, 0)
pi.set_PWM_dutycycle(22, 0)
pi.set_PWM_dutycycle(24, 0)

pi.stop()

