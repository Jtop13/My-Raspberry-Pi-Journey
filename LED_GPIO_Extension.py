import RPi.GPIO as GPIO
import time
GPIO.cleanup()

GPIO.setmode(GPIO.BCM)
GPIO.setup(23, GPIO.OUT)

blinks = int(input("How many times to blink led: "))

for i in range(blinks):	
	GPIO.output(23, True)
	time.sleep(0.2)
	GPIO.output(23, False)
	time.sleep(0.2)
	
GPIO.cleanup()
