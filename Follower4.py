import time
import RPi.GPIO as io
io.setmode(io.BCM)
io.setwarnings(False)
io.cleanup()
io.setup(3,io.IN)
io.setup(2,io.OUT)
io.setup(14,io.IN)
io.setup(15,io.OUT)
io.setup(5,io.OUT)
io.setup(6,io.OUT)
io.setup(13,io.OUT)
io.setup(19,io.OUT)
L2=io.PWM(5,250)
L1=io.PWM(6,250)
R2=io.PWM(13,250)
R1=io.PWM(19,250)
L1.start(0)
L2.start(0)
R1.start(0)
R2.start(0)
while 1:
	#-----------------------#
        io.output(2,io.LOW)
        time.sleep(0.00001)
        io.output(2,io.HIGH)
        time.sleep(0.00001)
        io.output(2,io.LOW)
        srt1=time.time()
        while io.input(3)==0 :
                srt1=time.time()
        while io.input(3)==1 :
                end1=time.time()
        t1=end1-srt1
        d1=(34300*t1)/2
	#-----------------------#
        io.output(15,io.LOW)
        time.sleep(0.00001)
        io.output(15,io.HIGH)
        time.sleep(0.00001)
        io.output(15,io.LOW)
        srt2=time.time()
        while io.input(14)==0 :
                srt2=time.time()
        while io.input(14)==1 :
                end2=time.time()
        t2=end2-srt2
        d2=(34300*t2)/2
	#-----------------------#
        if d1==20 :
                print " L STOP "
                L1.ChangeDutyCycle(0)
                L2.ChangeDutyCycle(0)
        elif d1>20 and d1<50 :
                print " L FWD 40 "
                L1.ChangeDutyCycle(40)
                L2.ChangeDutyCycle(0)
	elif d1>50 and d1<100 :
                print " L FWD 60 "
                L1.ChangeDutyCycle(60)
                L2.ChangeDutyCycle(0)
        elif d1>100 :
                print " L FWD 100 "
                L1.ChangeDutyCycle(80)
                L2.ChangeDutyCycle(0)
	elif d1<20 :
		print " L REV "
                L1.ChangeDutyCycle(0)
                L2.ChangeDutyCycle(40)
	#------------------------------#
        if d2==20 :
                print " R STOP "
                R1.ChangeDutyCycle(0)
                R2.ChangeDutyCycle(0)
        elif d2>20 and d2<50:
                print " R FWD 40 "
                R1.ChangeDutyCycle(40)
                R2.ChangeDutyCycle(0)
	elif d2>50 and d2<100:
                print " R FWD 60 "
                R1.ChangeDutyCycle(60)
                R2.ChangeDutyCycle(0)
        elif d2>100 :
                print " R FWD 80 "
                R1.ChangeDutyCycle(80)
                R2.ChangeDutyCycle(0)
        elif d2<20 :
                print " R REV "
                R1.ChangeDutyCycle(0)
                R2.ChangeDutyCycle(40)
	#------------------------------#
