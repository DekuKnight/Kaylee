#import smbus
import time

class Connection:

    #Constants
    DOOR_LOCK = 1
    DOOR_UNLOCK = 2
    LIGHTS_ON = 3
    LIGHTS_OFF = 4

    bus = None
    address = None

    def __init__(self):
        #self.bus = smbus.SMBus(1)
        self.address = 0x04
        
    def writeNumber(self,value):
        #bus.write_byte(self.address, value)
        print("Command %d sent to Arduino"%value)
        return -1

    def readNumber(self):
        number = bus.read_byte(self.address)
        return number
