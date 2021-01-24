import time
import RPi.GPIO as IO
IO.setmode(IO.BCM)
IO.setwarnings(False)
IO.cleanup()
IO.setup(2,IO.OUT)
P=IO.PWM(2,250)
P.start(0)
while 1:
	I=0
	while I<100 :
		P.ChangeDutyCycle(I)
		print "ON"
		I=I+1
		time.sleep(0.007)
	while I>0 :
		P.ChangeDutyCycle(I)
		print "OFF"
		I=I-1
		time.sleep(0.007)
