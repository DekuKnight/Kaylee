# GPIO

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setup(12, GPIO.OUT, initial=GPIO.HIGH)
time.sleep(2)
GPIO.output(12, GPIO.LOW)
time.sleep(2)
GPIO.output(12,GPIO.HIGH)
time.sleep(2)
GPIO.cleanup()
