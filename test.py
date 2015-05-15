from bean.MessageQueue import MessageQueue
from bean.Door import Door
from bean.Light import Light
from bean.Room import Room
from control.Processor import Processor
from control.Security import Security
from bean.User import User
import time

mq = MessageQueue()
p = Processor()
s = Security()
d = Door()
l = Light("Gypsy Danger")
l2 = Light("Arctic Monkey","on")
r = Room([l,l2],[d])

def executeMessages(messageQueue):
        if mq.refreshQueue():
            print("---Message Recieved!---")
            head = mq.pop()
            while head != None:
                print("---Message Recieved!---\n")
                if s.verify(head):
                    print("----" + getattr(head,"body"))
                    p.process(getattr(head,"body"),r)
                print("\n-----------------------")
                head = mq.pop()



try:
    while True:
        time.sleep(5)
        executeMessages(mq)
        
except KeyboardInterrupt:
    print "Goodbye"