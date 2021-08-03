import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

GPIO.setup(18,GPIO.OUT)

# GPIO.output(18,GPIO.HIGH)
# time.sleep(3)
# GPIO.cleanup()

p = GPIO.PWM(18,50)

for dc in range(0,101,5):
	p.start(dc)
	input('Press return to stop:')
p.stop()
GPIO.cleanup()
