class Message:
    
    sender = ""
    body = ""
    time = ""

    def __init__(self, data):
        self.sender = data[0]
        self.body = data[1]
        self.time = data[2]

    def toString(self):
        print ("Sender: %s Time: %s Message: %s" % (self.sender, self.time, self.body) )
        
