#!/usr/bin/env python

# Control Lasermodule from Raspberry Pi
# https://raspberrytips.nl/laser-module-aansturen-via-gpio/

import RPi.GPIO as GPIO
import time

LaserGPIO = 17 # --> PIN11/GPIO17

def setup():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(LaserGPIO, GPIO.OUT)
    GPIO.output(LaserGPIO, GPIO.HIGH)

def loop(identities):
    for person in identities:
        if person[0] != 'unknown':
                GPIO.output(LaserGPIO, GPIO.HIGH) # led on
                time.sleep(2.5)
    destroy()
def destroy():
    GPIO.output(LaserGPIO, GPIO.LOW)
    GPIO.cleanup()

def ready_laser(identifers):
    setup()
	loop(identifiers)

#try:
#    loop(identities)

#except KeyboardInterrupt:
#    destroy()
