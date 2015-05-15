#Project Jarvis
#Version 0 
#Author:	Ryan Wright
#Last Updated:	1 April 2013
#Project Description:
#	Functions: blink(void)
#	IO Pins used: 7(not really), 24
#	This project connects to the IO pins in the RPI and 
#	makes an LED blink 50 times. 

import RPi.GPIO as GPIO
import time

#blink function
def blink0():
        GPIO.output(24,GPIO.HIGH)
        time.sleep(1)
        GPIO.output(24,GPIO.LOW)
        time.sleep(1)
        return

def blink1():
	GPIO.output(24,GPIO.HIGH)
	time.sleep(.25)
	GPIO.output(24,GPIO.LOW)
	time.sleep(.25)
	return

def blink2():
        GPIO.output(24,GPIO.HIGH)
        time.sleep(.125)
        GPIO.output(24,GPIO.LOW)
        time.sleep(.125)
        return

#ignore warnings for now cause they're annoying me
GPIO.setwarnings(False)

#Use GPIO numbers not pin numbers
GPIO.setmode(GPIO.BCM)

#set up the GPIO channels - one input and one output
GPIO.setup(7, GPIO.IN)
GPIO.setup(24, GPIO.OUT)

#input from GPIO7
input_value = GPIO.input(7)


#loop blinks
for i in range (0, 50):
	blink2()
	blink1()
	blink2()
	print("blink")

GPIO.cleanup()
