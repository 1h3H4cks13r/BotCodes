import time
import RPi.GPIO as io
io.setmode(io.BCM)
io.setwarnings(False)
io.setup(5,io.OUT)
io.setup(6,io.OUT)
io.setup(13,io.OUT)
io.setup(19,io.OUT)
try:
	ch=raw_input(" KEY : ")
	if 
finally:
	io.output(10,io.LOW)
	io.cleanup()
