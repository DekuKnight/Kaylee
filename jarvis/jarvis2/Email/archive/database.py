import sqlite3
import time
import threading
from classes import User
from threading import Thread

#-----------User functions--------------
#addUser
def addUser(userName, userAdd, userPwd):
    userTuple = (userName,userAdd,userPwd,)
    c.execute('INSERT INTO users VALUES (?,?,?)', userTuple)
    conn.commit()
    
#delUser
def delUser(userName):
    name = (userName,)
    c.execute("DELETE FROM users WHERE name=(?)",name)
    conn.commit()

#changeUserPwd
def changeUserPwd(name, newPwd):
    changeTuple(name, newPwd,)
    c.execute("UPDATE users SET password=(?) where name=(?)",changeTuple)
    conn.commit()

#---------------Admin Functions-----------
#addAdmin
def addAdmin(adminName, adminAdd, adminPwd):
    adminTuple = (adminName,adminAdd,adminPwd,)
    c.execute('INSERT INTO admins VALUES (?,?,?)', adminTuple)
    conn.commit()
    
#delAdmin
def delAdmin(userName):
    name = (userName,)
    c.execute("DELETE FROM admins WHERE name=(?)",name)
    conn.commit()

#Change Admin pass
def changeAdminPwd(name, newPwd):
    changeTuple(name, newPwd,)
    c.execute("UPDATE admins SET password=(?) where name=(?)",changeTuple)
    conn.commit()

#---------------Temp Functions----------------
#addTemp
def addTemp(tempName, tempAdd):
    tempTuple = (tempName,tempAdd,)
    c.execute('INSERT INTO temps VALUES (?,?)', tempTuple)
    conn.commit()
    Thread(target = clearTemp, args=(tempName,)).start()
    
#clearTemp
def clearTemp(tempName):
    name = (tempName,)
    #wait 30 min?
    time.sleep(60)
    #delete temp user
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute("DELETE FROM temps WHERE name=(?)",name)
    dbShutdown(conn)
    print("tempUser %s deleted" % tempName)

def dbShutdown(connection):
    connection.commit()
    connection.close()
    
def returnUser(userPrompt):
    prompt = (userPrompt,)
    #Check if Admin
    c.execute("SELECT * FROM admins WHERE name=(?)",prompt)
    u = c.fetchone()
    if (u) == None:
        c.execute("SELECT * FROM admins WHERE address=(?)",prompt)
        u = c.fetchone()
        if (u) != None:
            return(User(u[0],u[1],u[2],0))
    else:
        return(User(u[0],u[1],u[2],0))

    #Check if User
    c.execute("SELECT * FROM users WHERE name=(?)",prompt)
    u = c.fetchone()
    if (u) == None:
        c.execute("SELECT * FROM users WHERE address=(?)",prompt)
        u = c.fetchone()
        if (u) != None:
            return(User(u[0],u[1],u[2],1))
    else:
        return(User(u[0],u[1],u[2],1))
        
    #Check if Temp
    c.execute("SELECT * FROM temps WHERE name=(?)",prompt)
    u = c.fetchone()
    if (u) == None:
        c.execute("SELECT * FROM temps WHERE address=(?)",prompt)
        u = c.fetchone()
        if (u) != None:
            return(User(u[0],u[1], None, 2))
    else:
        return(User(u[0],u[1], None, 2))

    return FAILURE

conn = sqlite3.connect('database.db')
c = conn.cursor()
newUser = returnUser("toadtoadt@gmail.com")
print(newUser.name, newUser.add, newUser.pwd, newUser.clearance)

dbShutdown(conn)
