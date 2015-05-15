from bean import *
from control import *
import time

class Kaylee:

    rooms = []
    p = Processor.Processor()

    def __init__(self,room=None):
        self.rooms.append(room)
    
    def executeMessages(self,mq):
        if mq.refreshQueue():
            head = mq.pop()
            while head != None:
                print("---Message Recieved!---\n")
                if Security.Security.verify(head):
                    Processor.Processor.process(getattr(head,"body"),self.rooms)
                print("\n-----------------------")
                head = mq.pop()

    def run(self):
        print("Hello!\n")
        mq = MessageQueue.MessageQueue()
        
        try:
            while True:
                time.sleep(5)
                self.executeMessages(mq)
        
        except KeyboardInterrupt:
            print("Goodbye")
        

if __name__== "__main__":
    
    d = Door.Door()
    l = Light.Light("Gypsy Danger")
    l2 = Light.Light("Arctic Monkey","on")
    room = Room.Room([l,l2],[d])
    k = Kaylee(room)
    k.run()
