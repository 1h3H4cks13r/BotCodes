import RPi.GPIO as io
import time
io.setmode(io.BCM)
io.setwarnings(False)
io.cleanup()
io.setup(17,io.IN)
io.setup(27,io.IN)
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
	IL=io.input(17)
        IR=io.input(27)
        if (IL==0) and (IR==0) :
        	print "REV"
                L2.ChangeDutyCycle(20)
                L1.ChangeDutyCycle(0)
                R2.ChangeDutyCycle(20)
                R1.ChangeDutyCycle(0)
        elif (IL==1) and (IR==0) :
                print "REV LEFT"
                L2.ChangeDutyCycle(0)
                L1.ChangeDutyCycle(0)
                R2.ChangeDutyCycle(95)
                R1.ChangeDutyCycle(0)
        elif (IL==0) and (IR==1) :
                print "REV RIGHT"
                L2.ChangeDutyCycle(95)
                L1.ChangeDutyCycle(0)
                R2.ChangeDutyCycle(0)
                R1.ChangeDutyCycle(0)
        elif (IL==1) and (IR==1) :
                print "STOP"
                L1.ChangeDutyCycle(0)
                L2.ChangeDutyCycle(0)
                R1.ChangeDutyCycle(0)
		R2.ChangeDutyCycle(0)
