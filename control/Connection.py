#import smbus
import time

class Connection

    bus = None
    address = None

    def __init__(self)
        #self.bus = smbus.SMBus(1)
        self.address = 0x04
        
    def writeNumber(value)
        #bus.write_byte(address, value)
        print(Command sent to Arduino)
        return -1


    def readNumber()
        number = bus.read_byte(address)
        return number