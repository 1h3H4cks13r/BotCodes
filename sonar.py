import time
import RPi.GPIO as io
io.setmode(io.BCM)
io.setwarnings(False)
io.cleanup()
io.setup(3,io.IN)
io.setup(2,io.OUT)
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
	end=time.time()
	t=end-srt
	d=(34300*t)/2
	print " DISTANCE : ",d

