import time
import RPi.GPIO as io

io.setmode(io.BCM)
io.setwarnings(False)
io.cleanup()
io.setmode(io.BCM)
io.setup(23,io.IN)
io.setup(24,io.IN)
io.setup(5,io.OUT)
io.setup(6,io.OUT)
io.setup(13,io.OUT)
io.setup(19,io.OUT)
L1=io.PWM(5,50)
L2=io.PWM(6,50)
R1=io.PWM(13,50)
R2=io.PWM(19,50)
L1.start(0)
L2.start(0)
R1.start(0)
R2.start(0)
while 1:
	IL=io.input(23)
	IR=io.input(24)
	if IL==0:
		if IR==0:
			print "FWD"
			L1.ChangeDutyCycle(40)
			L2.ChangeDutyCycle(0)
			R1.ChangeDutyCycle(45)
			R2.ChangeDutyCycle(0)
		elif IR==1:
			print "RIGHT"
			L1.ChangeDutyCycle(40)
			L2.ChangeDutyCycle(0)
			R1.ChangeDutyCycle(0)
			R2.ChangeDutyCycle(45)
	elif IL==1:
		if IR==0:
			print "LEFT"
			L1.ChangeDutyCycle(0)
			L2.ChangeDutyCycle(40)
			R1.ChangeDutyCycle(45)
			R2.ChangeDutyCycle(0)
		elif IR==1:
			print "STOP"
			L1.ChangeDutyCycle(0)
			L2.ChangeDutyCycle(0)
			R1.ChangeDutyCycle(0)
			R2.ChangeDutyCycle(0)
io.cleanup()

