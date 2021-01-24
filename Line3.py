import time
import RPi.GPIO as io

io.setmode(io.BCM)
io.setwarnings(False)
io.cleanup()
io.setmode(io.BCM)
io.setup(18,io.IN)
io.setup(15,io.IN)
io.setup(14,io.IN)
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
	IR=io.input(18)
	IM=io.input(15)
	IL=io.input(14)
	if (IL==0) and (IM==0) and (IR==0) :
		print "TURNING"
		L1.ChangeDutyCycle(0)
		L2.ChangeDutyCycle(60)
		R1.ChangeDutyCycle(60)
		R2.ChangeDutyCycle(0)
	elif IM==1:
		if IL==0:
			if IR==0:
				print "FWD"
				L1.ChangeDutyCycle(40)
				L2.ChangeDutyCycle(0)
				R1.ChangeDutyCycle(40)
				R2.ChangeDutyCycle(0)
			elif IR==1:
				print "RIGHT"
				L1.ChangeDutyCycle(40)
				L2.ChangeDutyCycle(0)
				R1.ChangeDutyCycle(0)
				R2.ChangeDutyCycle(40)
		elif IL==1:
			if IR==0:
				print "LEFT"
				L1.ChangeDutyCycle(0)
				L2.ChangeDutyCycle(40)
				R1.ChangeDutyCycle(40)
				R2.ChangeDutyCycle(0)
			elif IR==1:
				print "Pref-RIGHT"
				L1.ChangeDutyCycle(40)
				L2.ChangeDutyCycle(0)
				R1.ChangeDutyCycle(0)
				R2.ChangeDutyCycle(40)
	elif IM==0 :
		if (IL==0) and (IR==1):
                        print "RIGHT"
                        L1.ChangeDutyCycle(40)
                        L2.ChangeDutyCycle(0)
                        R1.ChangeDutyCycle(0)
                        R2.ChangeDutyCycle(40)
		elif (IL==1) and (IR==0):
                	print "LEFT"
                        L1.ChangeDutyCycle(0)
                        L2.ChangeDutyCycle(40)
                        R1.ChangeDutyCycle(40)
                        R2.ChangeDutyCycle(0)

