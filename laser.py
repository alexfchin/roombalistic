

#!/usr/bin/env python
#####################################################
#
#	DO NOT WATCH THE LASER DERECTELY IN THE EYE!
#
#####################################################
import RPi.GPIO as GPIO
import time

LedPin = 11    # pin11

def setup():
	GPIO.setmode(GPIO.BOARD)       # Numbers GPIOs by physical location
	GPIO.setup(LedPin, GPIO.OUT)   # Set LedPin's mode is output
	GPIO.output(LedPin, GPIO.HIGH) # Set LedPin high(+3.3V) to off led

def loop(identities):
	#identities = [('unknown', (107, 239, 159, 187)), ('Rahul Sondhi', (87, 156, 149, 93))]


	for person in identities:
		if person[0] != 'unknown':
			print('Laser on')
			#GPIO.output(LedPin, GPIO.LOW)  # led on
			time.sleep(1.0)
	destroy()
	# while True:
	# 	print '...Laser on'
	# 	GPIO.output(LedPin, GPIO.LOW)  # led on
	# 	time.sleep(0.5)
	# 	print 'Laser off...'
	# 	GPIO.output(LedPin, GPIO.HIGH) # led off
	# 	time.sleep(0.5)

def destroy():
	GPIO.output(LedPin, GPIO.HIGH)     # led off
	GPIO.cleanup()                     # Release resource

if __name__ == '__main__':     # Program start from here
	setup()
	try:
		loop()
	except KeyboardInterrupt:  # When 'Ctrl+C' is pressed, the child program destroy() will be  executed.
		destroy()

