import time
import RPi.GPIO as io
io.setmode(io.BCM)
io.setwarnings(False)
io.cleanup()
io.setup(3,io.IN)
io.setup(2,io.OUT)
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
        io.output(2,io.LOW)
        time.sleep(0.00001)
        io.output(2,io.HIGH)
        time.sleep(0.00001)
        io.output(2,io.LOW)
        srt=time.time()
        while io.input(3)==0 :
                srt=time.time()
        while io.input(3)==1 :
	        end=time.time()
        t=end-srt
        d=(34300*t)/2
        if (d>20) and (d<21) :
                print " STOP 00 "
                L1.ChangeDutyCycle(0)
                L2.ChangeDutyCycle(0)
                R1.ChangeDutyCycle(0)
                R2.ChangeDutyCycle(0)
        elif (d>20) and (d<30) :
                print " FWD 45  "
                L1.ChangeDutyCycle(40)
                L2.ChangeDutyCycle(0)
                R1.ChangeDutyCycle(40)
                R2.ChangeDutyCycle(0)
        elif (d>30) and (d<40):
                print " FWD 50 "
                L1.ChangeDutyCycle(45)
                L2.ChangeDutyCycle(0)
                R1.ChangeDutyCycle(45)
                R2.ChangeDutyCycle(0)
	elif (d>40) and (d<50):
                print " FWD 55  "
                L1.ChangeDutyCycle(50)
                L2.ChangeDutyCycle(0)
                R1.ChangeDutyCycle(50)
                R2.ChangeDutyCycle(0)
	elif(d>50) and (d<60):
                print " FWD 60 "
                L1.ChangeDutyCycle(55)
                L2.ChangeDutyCycle(0)
                R1.ChangeDutyCycle(55)
                R2.ChangeDutyCycle(0)
        elif(d>60) and (d<70):
                print " FWD 65 "
                L1.ChangeDutyCycle(60)
                L2.ChangeDutyCycle(0)
                R1.ChangeDutyCycle(60)
                R2.ChangeDutyCycle(0)
        elif (d>70) and (d<80) :
                print " FWD 70  "
                L1.ChangeDutyCycle(65)
                L2.ChangeDutyCycle(0)
                R1.ChangeDutyCycle(65)
                R2.ChangeDutyCycle(0)
        elif (d>80) and (d<90):
                print " FWD 75 "
                L1.ChangeDutyCycle(70)
                L2.ChangeDutyCycle(0)
                R1.ChangeDutyCycle(70)
                R2.ChangeDutyCycle(0)
        elif (d>90) and (d<100) :
                print " FWD 80  "
                L1.ChangeDutyCycle(75)
                L2.ChangeDutyCycle(0)
                R1.ChangeDutyCycle(75)
                R2.ChangeDutyCycle(0)
	elif d>100 :
                print " FWD 80  "
                L1.ChangeDutyCycle(80)
                L2.ChangeDutyCycle(0)
                R1.ChangeDutyCycle(80)
                R2.ChangeDutyCycle(0)
	elif d<20 :
		print " REV "
		L1.ChangeDutyCycle(0)
                L2.ChangeDutyCycle(40)
                R1.ChangeDutyCycle(0)
                R2.ChangeDutyCycle(40)
