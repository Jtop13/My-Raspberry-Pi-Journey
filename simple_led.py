import RPi.GPIO as GPIO
import time
GPIO.cleanup()

GPIO.setmode(GPIO.BOARD)
GPIO.setup(11, GPIO.OUT)

blinks = int(input("How many times to blink led: "))

for i in range(blinks):	
	GPIO.output(11, True)
	time.sleep(0.2)
	GPIO.output(11, False)
	time.sleep(0.2)
	
GPIO.cleanup()
