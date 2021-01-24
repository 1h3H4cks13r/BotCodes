import RPi.GPIO as io
import time
import curses
io.setmode(io.BCM)
io.setwarnings(False)
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
stdscr=curses.initscr()
curses.noecho()
curses.cbreak()
while 1:
	ch=stdscr.getch()
	if ch==ord('w'):
		print "FWD"
        	L1.ChangeDutyCycle(70)
		L2.ChangeDutyCycle(0)
		R1.ChangeDutyCycle(70)
		R2.ChangeDutyCycle(0)
		time.sleep(0.03)
	elif ch==ord('a'):
		print "LEFT"
	        L1.ChangeDutyCycle(0)
		L2.ChangeDutyCycle(0)
		R1.ChangeDutyCycle(100)
		R2.ChangeDutyCycle(0)
		time.sleep(0.03)
	elif ch==ord('d'):
               	print "RIGHT"
	        L1.ChangeDutyCycle(100)
                L2.ChangeDutyCycle(0)
	        R1.ChangeDutyCycle(0)
                R2.ChangeDutyCycle(0)
               	time.sleep(0.03)
	elif ch==ord('s'):
		print "REV"
        	L1.ChangeDutyCycle(0)
		L2.ChangeDutyCycle(40)
		R1.ChangeDutyCycle(0)
		R2.ChangeDutyCycle(40)
		time.sleep(0.03)
	elif ch==ord('q'):
                L1.ChangeDutyCycle(0)
                L2.ChangeDutyCycle(100)
                R1.ChangeDutyCycle(0)
                R2.ChangeDutyCycle(0)
                time.sleep(0.03)
	elif ch==ord('e'):
                L1.ChangeDutyCycle(0)
                L2.ChangeDutyCycle(0)
                R1.ChangeDutyCycle(0)
                R2.ChangeDutyCycle(100)
                time.sleep(0.03)
	elif ch==ord('x'):
		print "STOP"
		L1.ChangeDutyCycle(0)
		L2.ChangeDutyCycle(0)
		R1.ChangeDutyCycle(0)
		R2.ChangeDutyCycle(0)
		break
	else :
		pass
	L1.ChangeDutyCycle(0)
	L2.ChangeDutyCycle(0)
	R1.ChangeDutyCycle(0)
	R2.ChangeDutyCycle(0)
curses.nocbreak(); curses.echo()
curses.endwin()
io.cleanup()
