from bean.Connection import Connection

class Door:

    conn = Connection()
    state = "locked"

    def __init__(self, state = "locked"):
        self.state = state

    def toString(self):
        print("The door is %s" % self.state)        

    def lock(self):
        if(self.state == "locked"):
            print("Door already locked")
        else:
            self.conn.writeNumber(Connection.DOOR_LOCK)
            self.state= "locked"
            self.toString()

    def unlock(self):
        if(self.state == "unlocked"):
            print("Door already unlocked")
        else:
            self.conn.writeNumber(Connection.DOOR_UNLOCK)
            self.state= "unlocked"
            self.toString()

    def toggle(self):
        if(self.state == "locked"):
            self.conn.writeNumber(Connection.DOOR_UNLOCK)
            self.state = "unlocked"
        elif(self.state == "unlocked"):
            self.conn.writeNumber(Connection.DOOR_LOCK)
            self.state = "locked"
        else:
            self.conn.writeNumber(Connection.DOOR_LOCK)
            self.state = "locked"
        self.toString()
