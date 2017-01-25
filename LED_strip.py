import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)

GPIO.setup(17, GPIO.OUT) #Control de la led bleu
GPIO.setup(24, GPIO.OUT) #Control de la led rouge
GPIO.setup(22, GPIO.OUT) #Control de la led verte

r = GPIO.PWM(17, 100)
g = GPIO.PWM(22, 100)
b = GPIO.PWM(24, 100)

r.start(0)
g.start(0)
b.start(0)

try:

        while True:
            for i in range(100):
		r.ChangeDutyCycle(i)
		r.ChangeDutyCycle(i)
		r.ChangeDutyCycle(i)
		time.sleep(5)


except KeyboardInterrupt:
    pass

GPIO.cleanup()

