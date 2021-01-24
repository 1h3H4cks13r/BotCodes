import RPi.GPIO as io
import time
io.setmode(io.BCM)
io.setwarnings(False)
io.cleanup()
io.setup(2,io.IN)
io.setup(3,io.IN)
io.setup(5,io.OUT)
io.setup(6,io.OUT)
io.setup(13,io.OUT)
io.setup(19,io.OUT)
L1=io.PWM(5,250)
L2=io.PWM(6,250)
R1=io.PWM(13,250)
R2=io.PWM(19,250)
L1.start(0)
L2.start(0)
R1.start(0)
R2.start(0)
while 1:
	IL=io.input(2)
	IR=io.input(3)
	if (IL==0) and (IR==0) :
		print "FWD"
        	L1.ChangeDutyCycle(30)
		L2.ChangeDutyCycle(0)
		R1.ChangeDutyCycle(30)
		R2.ChangeDutyCycle(0)
	elif (IL==1) and (IR==0) :
		print "LEFT"
	        L1.ChangeDutyCycle(0)
		L2.ChangeDutyCycle(0)
		R1.ChangeDutyCycle(90)
		R2.ChangeDutyCycle(0)
	elif (IL==0) and (IR==1) :
               	print "RIGHT"
	        L1.ChangeDutyCycle(90)
                L2.ChangeDutyCycle(0)
	        R1.ChangeDutyCycle(0)
                R2.ChangeDutyCycle(0)
	elif (IL==1) and (IR==1) :
		print "STOP"
        	L1.ChangeDutyCycle(0)
		L2.ChangeDutyCycle(0)
		R1.ChangeDutyCycle(0)
		R2.ChangeDutyCycle(0)

