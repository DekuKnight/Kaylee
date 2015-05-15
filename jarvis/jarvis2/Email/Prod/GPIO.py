#GPIO

try:
    import RPi.GPIO as GPIO
except RuntimeError:
    print("something happened")
