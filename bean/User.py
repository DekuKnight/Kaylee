class User:

    name = ""
    address = ""
    number = ""
    carrier = ""
    password = ""
    isActive = True
    isAdmin = False

    def __init__(self, name="", number="", carrier="", password="",isAdmin=False):
        self.name = name
        self.address = number + "@" + carrier
        self.number = number
        self.carrier = carrier
        self.password = password
        self.isActive = True
        self.isAdmin = isAdmin

    def toString(self):
        if self.isAdmin:
            user = "Admin"
        else:
            user = "User"
        print( "%s %s \n  Address: %s\n  Password: %s\n  Active: %r" % (user, self.name, self.address, self.password, self.isActive) )

    def toggleActive(self):
        if self.isActive:
            self.isActive = False
        else:
            self.isActive = True