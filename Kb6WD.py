import RPi.GPIO as io
import time
import curses
io.setmode(io.BCM)
io.setwarnings(False)
io.setup(10,io.OUT)
io.setup(9,io.OUT)
io.setup(11,io.OUT)
io.setup(0,io.OUT)
io.setup(5,io.OUT)
io.setup(6,io.OUT)
io.setup(13,io.OUT)
io.setup(19,io.OUT)
L1=io.PWM(5,250)
L2=io.PWM(6,250)
L3=io.PWM(10,250)
L4=io.PWM(9,250)
R1=io.PWM(13,250)
R2=io.PWM(19,250)
R3=io.PWM(11,250)
R4=io.PWM(0,250)
L1.start(0)
L2.start(0)
L3.start(0)
L4.start(0)
R1.start(0)
R2.start(0)
R3.start(0)
R4.start(0)
stdscr=curses.initscr()
curses.noecho()
curses.cbreak()
while 1:
	ch=stdscr.getch()
	if ch==ord('w'):
		print "FWD"
        	L1.ChangeDutyCycle(40)
		L2.ChangeDutyCycle(0)
		L3.ChangeDutyCycle(40)
		L4.ChangeDutyCycle(0)
		R1.ChangeDutyCycle(40)
		R2.ChangeDutyCycle(0)
		R3.ChangeDutyCycle(40)
		R4.ChangeDutyCycle(0)
	elif ch==ord('a'):
		print "LEFT"
	        L1.ChangeDutyCycle(20)
		L2.ChangeDutyCycle(0)
		L3.ChangeDutyCycle(20)
		L4.ChangeDutyCycle(0)
		R1.ChangeDutyCycle(60)
		R2.ChangeDutyCycle(0)
		R3.ChangeDutyCycle(60)
		R4.ChangeDutyCycle(0)
	elif ch==ord('s'):
		print "REV"
        	L1.ChangeDutyCycle(0)
		L2.ChangeDutyCycle(40)
		L3.ChangeDutyCycle(0)
		L4.ChangeDutyCycle(40)
		R1.ChangeDutyCycle(0)
		R2.ChangeDutyCycle(40)
		R3.ChangeDutyCycle(0)
		R4.ChangeDutyCycle(40)
	elif ch==ord('d'):
		print "RIGHT"
		L1.ChangeDutyCycle(60)
		L2.ChangeDutyCycle(0)
		L3.ChangeDutyCycle(60)
		L4.ChangeDutyCycle(0)
		R1.ChangeDutyCycle(20)
		R2.ChangeDutyCycle(0)
		R3.ChangeDutyCycle(20)
		R4.ChangeDutyCycle(0)
	elif ch==ord('x'):
		print "STOP"
		L1.ChangeDutyCycle(0)
		L2.ChangeDutyCycle(0)
		L3.ChangeDutyCycle(0)
		L4.ChangeDutyCycle(0)
		R1.ChangeDutyCycle(0)
		R2.ChangeDutyCycle(0)
		R3.ChangeDutyCycle(0)
		R4.ChangeDutyCycle(0)
	elif ch==ord('q'):
		break
print "Broken"
curses.nocbreak(); curses.echo()
curses.endwin()
io.cleanup()
l
