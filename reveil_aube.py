import pigpio
import time

#pin 17 = rouge
#pin 22 = vert
#pin 24 = bleu


RED_PIN = 17
GREEN_PIN = 22
BLUE_PIN = 24

try:
    
	user_time = int(input("Pendant combien de minutes doit-il s'allumer : "))

#def temps(user_time):

	user_seconds = user_time*60
	time_sleep= user_seconds/255
    
 #   return time_sleep


	pi = pigpio.pi()


	while True:
		for i in range(2, 255):
			pi.set_PWM_dutycycle(RED_PIN, i)
			pi.set_PWM_dutycycle(BLUE_PIN, i)
			pi.set_PWM_dutycycle(GREEN_PIN, i)
			time.sleep(time_sleep)
	    
except KeyboardInterrupt:
    pass

pi.set_PWM_dutycycle(RED_PIN, 0)
pi.set_PWM_dutycycle(BLUE_PIN, 0)
pi.set_PWM_dutycycle(GREEN_PIN, 0)

pi.stop()
