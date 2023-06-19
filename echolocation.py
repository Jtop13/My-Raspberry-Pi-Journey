import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)

trigPin = 23
echoPin = 24

GPIO.setup(trigPin,GPIO.OUT)
GPIO.setup(echoPin,GPIO.IN)

try:
	while True:
		#print("Hit")
		GPIO.output(trigPin, 0)
		time.sleep(2E-6)
		GPIO.output(trigPin, 1)
		time.sleep(10E-6)
		GPIO.output(trigPin, 0)
		while GPIO.input(echoPin) == 0:
			#print("Wait for ping to leave sensor")
			pass
		echoStartTime=time.time()
		while GPIO.input(echoPin) == 1:
			#print("Ping has left sensor")
			pass
		echoStopTime=time.time()
		#print("Ping has come back")
		
		pingTravelTime = echoStopTime-echoStartTime	
		#print(int(pingTravelTime*1E6))
		#Distance
		pingTravel = round(float(pingTravelTime * 343), 4)
		print(str(pingTravel) + " Meters")
		time.sleep(0.2)
except KeyboardInterrupt:
	GPIO.cleanup()
	print("Finished")
