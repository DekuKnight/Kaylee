from bean.Connection import Connection

class Light:

    conn = Connection()
    name = ""
    state = "off"

    def __init__(self, name="",state="off"):
        if name != "":
            self.name = name + " "
        else:
            self.name = name
        self.state = state

    def toString(self):
        print("Light %sis %s" % (self.name,self.state) )

    def off(self):
        if(self.state == "off"):
            print("Light %salready off" % self.name)
        else:
            self.conn.writeNumber(Connection.LIGHTS_OFF)
            self.state = "off"
            self.toString()

    def on(self):
        if(self.state == "on"):
            print("Light %salready on" % self.name)
        else:
            self.conn.writeNumber(Connection.LIGHTS_ON)
            self.state = "on"
            self.toString()
            
    def toggle(self):
        if(self.state == "on"):
            self.conn.writeNumber(Connection.LIGHTS_OFF)
            self.state = "off"
        elif(self.state == "off"):
            self.conn.writeNumber(Connection.LIGHTS_ON)
            self.state = "on"
        else:
            self.conn.writeNumber(Connection.LIGHTS_OFF)
            self.state = "off"
        self.toString()
