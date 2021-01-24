import RPi.GPIO as io
io.setmode(io.BCM)
io.setwarnings(False)
io.setup(2,io.IN)
while 1:
	if io.input(2)==0 :
		print '0'
	elif io.input(2)==1 :
		print '1'
