#----------------------------------------------------------------------
#||  Project Jarvis
#||  Version 2.0
#||
#||  Author:         Ryan Wright
#||  Email:          rdwright5127@gmail.com
#||  Last Modified:  12.6.13
#||
#||  File Description: functions.py
#||      This file contains most of the functions that will be used
#||      in the program. They are organized by type:
#||          -Mail Functions
#||          -User List Functions
#||          -Mode Functions
#||          -Input Cleanup Function
#||      Further descriptions are in the subsets below
#||      


import imaplib
import email
import os
import smtplib
import time
import sqlite3
import threading
from threading import Thread
from optparse import OptionParser

class DatabaseManager(object):
    def __init__(self, db):
        self.conn = sqlite3.connect(db)
        self.cur = self.conn.cursor()

    def execute(self, arg):
        self.cur.execute(arg)
        self.conn.commit()
        return self.cur

    def query(self, arg):
        self.cur.execute(arg[0],arg[1])
        self.conn.commit()
        return self.cur

    def printDB(self):
        adminList = getAdminList()
        userList = getUserList()
        tempList = getTempList()
        print("Admins:")
        for admin in adminList:
            print(admin)
        print("Users:")
        for user in userList:
            print(user)
        print("Temps:")
        for temp in tempList:
            print(temp)

    def __del__(self):
        self.conn.close()

class User:
    name = ""
    add = ""
    pwd = ""
    clearance = ""
    
    def __init__(self):
        self.name = "name"
        self.add = "add"
        self.pwd = "pwd"
        self.clearance = "clearance"

    def __init__(self, name, add, pwd, clearance):
        self.name = name
        self.add = add
        self.pwd = pwd
        self.clearance = clearance

    def print(self):
        print(self.name, self.add, self.pwd, self.clearance)

    def changePwd(self,newPwd):
        self.pwd = newPwd
        if self.clearance == ADMIN:
            changeAdminPwd(self.name,newPwd)
        else: #is a user
            changeUserPwd(self.name,newPwd)


#Just some various Constants & classes
ADMIN, USER, TEMP = 0, 1, 2
NO_MESSAGE = 'No new messages'
SUCCESS, FAILURE, CRAP = 1, -1, 0
ON, OFF, NULL = 1, -1, 0
dbManager = DatabaseManager("database.db")
TEMP_TIME = (30)*60
RAGE_PARROT = 50


#                   --Mail Functions--
#   Functions involving the IMAP and SMTP processes of recieving
#   and sending emails. Don't mess with these unless you really have
#   to cause they were a pain to get to work. Functions include:
#       -getprompt()
#       -sendmsg(varTo, varMsg, varUser = 'jarvis104Mckee@gmail.com', varPass = 'jarvis104',verbose)
#

#Goes to the gmail account and gets the most recent unread email
#IN: Nothing
#OUT: msgTuple = [AddressOfSender, Message]
def getprompt():
    USER = 'jarvis104Mckee@gmail.com'
    PASSWORD = 'jarvis104'

    mail = imaplib.IMAP4_SSL('imap.gmail.com')
    mail.login(USER,PASSWORD)

    mail.select('Inbox')

    resp, data = mail.search(None, 'UnSeen')

    nullMsg = data[0].decode('utf-8')
    if nullMsg == '':
        return('No new messages')
    
    for num in (data[0].split()):
      resp, msg = mail.fetch(num, '(RFC822)')

      for response_part in msg:
          if isinstance(response_part, tuple):
              message = email.message_from_bytes(response_part[1])
              varFrom = message['from']

              for part in message.walk():
                  if part.get_content_type() == 'text/plain':
                      varBody = part.get_payload(decode=True)

                      #remove the brackets around the sender email address
                      head = varFrom.find('<')
                      varFrom = varFrom[head+1:]
                      varFrom = varFrom.replace('>', '')

                      #decode the body and make it pretty
                      varBody = varBody.decode('utf-8')
                        #for ATT
                      varBody = varBody.replace("\r\n--\r\n==================================================================\r\nThis mobile text message is brought to you by AT&T\r\n",'')

                        #for VTEXT
                      varBody = varBody.replace("\r\n",'')

                  elif part.get_content_type() == 'text/html':
                      varBody = part.get_payload(decode=True)
                      varBody = varBody.decode('utf-8')
                      head = varBody.find('<td>')
                      tail = varBody.rfind('</td>')
                      varBody = varBody[head+4:tail]
                      varBody = varBody.replace("\r\n","")
                      varBody = varBody.strip()
                      
                  else:
                      continue
    msgTuple = [varFrom, varBody] 
    mail.close()
    mail.logout()
    return(msgTuple)

#Sends a message
#IN: varTo = Address to send from, varMsg = Message to send
#OUT: Success or failure
def sendmsg(varTo, varMsg, Verbose, varUser = 'jarvis104Mckee@gmail.com', varPass = 'jarvis104'):
    #Set variables
    to = varTo
    gmail_user = varUser
    gmail_pwd = varPass

    try:
        #Login
        smtpserver = smtplib.SMTP("smtp.gmail.com",587)
        smtpserver.ehlo()
        smtpserver.starttls()
        smtpserver.ehlo
        smtpserver.login(gmail_user, gmail_pwd)
            
        msg = "\r\n".join(["From: Jarvis","To: " + varTo,"A message From Jarvis","",varMsg,""])
        printmsg = "\r\n--->".join(["From: Jarvis","To: " + varTo,"A message From Jarvis","",varMsg,""])
    except smtplib.SMTPException as e:
        print("Something went wrong with connecting to the server")
        print(e)
    try:
        smtpserver.sendmail(gmail_user, to, msg.encode('utf-8'))
        verbose("Message sent to %s"%(to),2,Verbose)
        verbose(printmsg,3,Verbose)
    except smtplib.SMTPException as e:
        print("Something went wrong with sending a reply to %s" %to)
        print(e)
    smtpserver.close()
    return



#                           --Mode Functions--
#   Mode Functions describe and execute the different types of modes that
#   the program is capable of. See modeArray.txt in the archive folder for
#   a full list as well as a descriptionof the modeArray itself. These should
#   be the only functions that take in the modeArray because they are editing it.
#   The mode array is just a list of numbers/boolean values (tuple in future?)
#   All others in other categories should pass by value. Functions include:
#       -verboseCount(userMsg, modeArray)
#       -toggleParrotMode(userMsg,modeArray)
#       -toggleRageParrotMode(userMsg, modeArray)
#       -getModeArrayDefaults()
#   Note: When these functions are finished the message will no longer have those
#   words/values in them. Ex. "password i like -v pie -v" >>> "password i like pie"
#

#Counts the number of verbose flags in the message
#IN: takes in the message and the modeArray

def verboseCount(userMsg, modeArray):
    modeArray[0] = userMsg.count("-v") + modeArray[0]
    if modeArray[0] > 0:
        print("Verbose mode activated:\nVerbose Level " + str(modeArray[0]) +"\n")
    return(userMsg.replace('-v',''))

def verbose(msg,verboseLevel,currentLevel):
    if currentLevel >= verboseLevel:
        n=0
        while n != verboseLevel:
            n += 1
            print('-',end='')
        print('>%s'%msg)
    else:
        return

#toggles the ParrotMode
#IN:  takes in the message and the modeArray
#OUT: returns the message string
def toggleParrotMode(userMsg,modeArray):
    message = userMsg.split()
    for msg in message:
        if msg == "parrotMode":
            modeArray[1] = not modeArray[1]
            if not modeArray[1]:
                print("Parrot Mode Deactivated\n")
            else: #parrotMode == False
                print("Parrot Mode Activated\n")
    return(userMsg.replace('parrotMode', ''))

#toggles the RageParrotMode
#IN:  takes in the message and the modeArray
#OUT: returns the message string
def toggleRageParrotMode(userMsg,modeArray):
    message = userMsg.split()
    for msg in message:
        if msg == "rageParrotMode":
            modeArray[2] = not modeArray[2]
            if not modeArray[2]:
                print("Parrot Mode Deactivated\n")
            else: #parrotMode == False
                print("PARROT MODE ACTIVATED!!!\n")
    return(userMsg.replace('rageParrotMode', ''))

def parrot(prompt, modeArray):
    #parrotMode
    if modeArray[1] == True:
        sendmsg(prompt[0],prompt[1]+' SQUAWK',modeArray[0])
    #rageParrotMode
    if modeArray[2] == True:
        sendmsg(prompt[0],"rageParrotMode is active but I'm not going to activate it yet. You're welcome.",modeArray[0])
#        while i != 50:
#            i = i + 1
#            sendmsg(prompt[0],prompt[1]+' SQUAWK')
    return

def toggleQuietMode(userMsg,modeArray):
    message = userMsg.split()
    for msg in message:
        if msg == "hush":
            modeArray[3] = not modeArray[3]
            if not modeArray[3]:
                print("Quiet Mode Deactivated\n")
            else: #parrotMode == False
                print("Quiet Mode Activated.\n")
    return(userMsg.replace('hush', ''))

def speak(msg,to, modeArray):
    if modeArray[3]:
        return
    else:
        sendmsg(to, msg, modeArray[0])

#Sets up the default values for the modeArray
#Slated for getting rid of, used for debugging
#IN: None
#OUT: modeArray
def getModeArrayDefaults():
    verbose = 2
    parrotMode = False
    rageParrotMode = False
    quiet = False
    modeArray = [verbose,parrotMode,rageParrotMode,quiet]
    return(modeArray)

def parseOpt(modeArray):
    parser = OptionParser()
    parser.add_option("-v", action="count", dest="verbose", default=0, help="verbose count")
    parser.add_option("-q", action="store_true", dest="quiet",default=True, help="quiet mode")
    parser.add_option("-p","--parrot", action="store_true", dest="parrotMode", default=False, help="parrot mode")
    parser.add_option("-r","--rage", action="store_true", dest="rageParrotMode", default=False, help="rage parrot Mode")

    (options, args) = parser.parse_args()

    modeArray[0] = options.verbose + modeArray[0]
    modeArray[1] = options.parrotMode + modeArray[1]
    modeArray[2] = options.rageParrotMode + modeArray[2]
    modeArray[3] = options.quiet + modeArray[3]
    
#        --Input Cleanup Function--
#executes the prompt described in newPrompt
#IN:  newPrompt variable, verbose flag
#OUT: Success flag if successful
def conditionPrompt(newPrompt, modeArray):
    errormsg = "Somethin' strange happened!"
    
    if modeArray[0] > 1:
        print
    #cleanup the prompt
    #Toggle ParrotMode
    newPrompt[1] = toggleParrotMode(newPrompt[1], modeArray)

    #Toggle RageParrotMode
    newPrompt[1] = toggleRageParrotMode(newPrompt[1], modeArray)
    
    #verbose flag
    newPrompt[1] = verboseCount(newPrompt[1],modeArray)

    #quiet flag

    verbose("Extracting Variables...\n",2,modeArray[0])

    #Extract variables from prompt
    varPrompt = newPrompt[1]
    varUser = returnUser(newPrompt[0])
            
    #Check if user is on the userList
    if varUser == FAILURE:
        tempUser = User("MysteryMan",newPrompt[0],"VOID",3)
        errormsg = "You are not a user. You have been rejected."
        return([FAILURE,errormsg,tempUser])

    print("User %s has sent a prompt\n" %varUser.name)
    verbose(("Prompt sent: %s\n" %varPrompt),2,modeArray[0])

    #Split up the prompt into separate words(units)
    units = varPrompt.split()
    
    #units will typically work as follows:
    # <password> <command> <additional parameters>

    promptPass = None
    command = None
    paramList = []

    verbose("Formatting prompt...",2,modeArray[0])
    if len(units) >= 3:
        for unit in units[2:]:
            paramList.append(unit)
        command = units[1]
    elif len(units) >= 2:
        paramList.append("Empty")
        command = units[1]
    elif len(units) >= 1:
        promptPass = units[0]
    else:
        errormsg = "Empty prompt"
        return([FAILURE,errormsg,varUser])
    
    if units[0] != varUser.pwd: #password is not the same
        errormsg = "Wrong Password. Try again."
        return([FAILURE,errormsg,varUser])

    #create responding tuple
    #   function status, promptTuple = [command, parameter array]
    resultTuple = [SUCCESS, [command,paramList], varUser]
    
    return resultTuple



#--------------DATABASE FUNCTIONS-----------------------
#-----------User functions--------------
#addUser
def addUser(userName, userAdd, userPwd):
    userTuple = (userName,userAdd,userPwd,)
    dbManager.query(('INSERT INTO users VALUES (?,?,?)', userTuple))
    
#delUser
def delUser(userName):
    name = (userName,)
    dbManager.query(("DELETE FROM users WHERE name=(?)",name))

#changeUserPwd
def changeUserPwd(name, newPwd):
    changeTuple = (newPwd, name,)
    dbManager.query(("UPDATE users SET password=(?) where name=(?)",changeTuple))

#send a message to the users
def notifyUsers(msg):
    userList = getUserList()
    for user in userList:
        sendmsg(user[1],msg,0)

#get a list with all users
def getUserList():
    userList = []
    dbManager.execute("SELECT * FROM users")
    user = dbManager.cur.fetchall()
    for u in user:
        userList.append(u)
    return userList    

#---------------Admin Functions-----------
#addAdmin
def addAdmin(adminName, adminAdd, adminPwd):
    adminTuple = (adminName,adminAdd,adminPwd,)
    dbManager.query(('INSERT INTO admins VALUES (?,?,?)', adminTuple))
    
#delAdmin
def delAdmin(userName):
    name = (userName,)
    dbManager.query(("DELETE FROM admins WHERE name=(?)",name))
    conn.commit()

#Change Admin pass
def changeAdminPwd(name, newPwd):
    changeTuple = (newPwd, name,)
    dbManager.query(("UPDATE admins SET password=(?) where name=(?)",changeTuple))

#send a message to the admins
def notifyAdmins(msg):
    adminList = getAdminList()
    for admin in adminList:
        sendmsg(admin[1],msg,0)

#get a list with the admin's addresses
def getAdminList():
    adminList = []
    dbManager.execute("SELECT * FROM admins")
    admin = dbManager.cur.fetchall()
    for a in admin:
        adminList.append(a)
    return adminList
    
#---------------Temp Functions----------------
#addTemp
def addTemp(tempName, tempAdd):
    tempTuple = (tempName,tempAdd,)
    dbManager.query(('INSERT INTO temps VALUES (?,?)', tempTuple))
    Thread(target = clearTemp, args=(tempName,)).start()
    
#clearTemp
def clearTemp(tempName):
    name = (tempName,)
    #wait 30 min?
    time.sleep(60)
    #delete temp user
    tempManager = DatabaseManager("database.db")
    tempManager.query(("SELECT * FROM temps WHERE name=(?)",name))
    returnAdd = (tempManager.cur.fetchone())[1]
    tempManager.query(("DELETE FROM temps WHERE name=(?)",name))
    print("tempUser %s deleted" % tempName)
    sendmsg(returnAdd,"You have been removed from Jarvis' mainframe. Have a nice day!",2)

#get a list with the temp's addresses
def getTempList():
    tempList = []
    dbManager.execute("SELECT * FROM temps")
    temp = dbManager.cur.fetchall()
    for t in temp:
        tempList.append(t)
    return tempList

#clears the temp list
def clearTemps():
    dbManager.execute("DELETE FROM temps")
    print("Temp List cleared")

#----------------General User Functions---------------------

def notifyErrybody(msg):
    masterList = []
    adminList = getAdminList()
    userList = getUserList()
    tempList = getTempList()
    for admin in adminList:
        masterList.append(admin)
    for user in userList:
        masterList.append(user)
    for temp in tempList:
        masterList.append(temp)
    for user in masterList:
        #sendmsg(user[1],msg,0)
        print(user)
    
def returnUser(userPrompt):
    prompt = (userPrompt,)
    #Check if Admin
    dbManager.query(("SELECT * FROM admins WHERE name=(?)",prompt))
    u = dbManager.cur.fetchone()
    if (u) == None:
        dbManager.query(("SELECT * FROM admins WHERE address=(?)",prompt))
        u = dbManager.cur.fetchone()
        if (u) != None:
            return(User(u[0],u[1],u[2],ADMIN))
    else:
        return(User(u[0],u[1],u[2],ADMIN))

    #Check if User
    dbManager.query(("SELECT * FROM users WHERE name=(?)",prompt))
    u = dbManager.cur.fetchone()
    if (u) == None:
        dbManager.query(("SELECT * FROM users WHERE address=(?)",prompt))
        u = dbManager.cur.fetchone()
        if (u) != None:
            return(User(u[0],u[1],u[2],USER))
    else:
        return(User(u[0],u[1],u[2],USER))
        
    #Check if Temp
    dbManager.query(("SELECT * FROM temps WHERE name=(?)",prompt))
    u = dbManager.cur.fetchone()
    if (u) == None:
        dbManager.query(("SELECT * FROM temps WHERE address=(?)",prompt))
        u = dbManager.cur.fetchone()
        if (u) != None:
            return(User(u[0],u[1], None, TEMP))
    else:
        return(User(u[0],u[1], None, TEMP))

    return FAILURE

def shutdown():
    clearTemps()
    print("Goodbye Sir!")
    time.sleep(2)

    
