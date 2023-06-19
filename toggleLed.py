from time import sleep
import RPi.GPIO as GPIO
delay = 0.1
inPin = 40
outPin = 38

GPIO.setmode(GPIO.BOARD)
GPIO.setup(38, GPIO.OUT)
GPIO.setup(40, GPIO.IN, pull_up_down=GPIO.PUD_UP)
LEDstate = 0
buttonState = 1
buttonStateOld = 1

try:
	while True:
		buttonState=GPIO.input(38)
		print(buttonState)
		if buttonState==1 and buttonStateOld==0:
			LEDstate = not LEDstate
			GPIO.output(38,LEDstate)
		buttonStateOld = buttonState	
		sleep(delay)
except KeyboardInterrupt:
	GPIO.cleanup()
	print("Finished")
