from control.MailHandler import MailHandler
from collections import deque

class MessageQueue:

    messages = deque()

    def __init__(self,messages = []):
        self.messages = deque(messages)

    def toString(self):
        for msg in self.messages:
            msg.toString()

    def pop(self):
        if self.messages:
            return self.messages.popleft()
        else:
            return None

    def refreshQueue(self):
        mg = MailHandler()
        newMsgs = mg.getMail()
        for msg in newMsgs:
            self.messages.append(msg)
        if self.messages:
            return True
        else:
            return False
