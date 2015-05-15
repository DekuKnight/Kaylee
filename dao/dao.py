import sqlite3

class dao:
    #Constructor
    def __init__(self, db = "dao/database.db"):
        self.conn = sqlite3.connect(db)
        self.cur = self.conn.cursor()
        
    #Executes a sql statement without any arguments
    def execute(self, arg):
        self.cur.execute(arg)
        self.conn.commit()
        return self.cur

    #Executes a sql statement with arguments
    def query(self, arg):
        self.cur.execute(arg[0],arg[1])
        self.conn.commit()
        return self.cur

    #Prints the entire database
    def printDB(self):
        for row in self.execute("Select * from users"):
            print(row)

    
    #Destructor
    def __del__(self):
        self.conn.close()

if __name__ == "__main__":
    #setup database
    dao = dao("database.db")
    try:
        dao.execute("DROP TABLE users")
    except(Error):
        pass
    dao.execute('''CREATE TABLE users(name text, password text, address text)''')
    dao.execute("INSERT INTO users (name, password, address) VALUES (\"Ryan\",\"x\",\"4846808235@mms.att.net\")")
    dao.execute("INSERT INTO users (name, password, address) VALUES (\"Eric\",\"x\",\"8143414844@vtext.com\")")
    dao.conn.commit()
    dao.printDB()