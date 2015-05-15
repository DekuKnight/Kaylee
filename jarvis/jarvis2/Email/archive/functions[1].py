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
#||      Further descriptions are in the subsets below
#||      


import imaplib
import email
import os
import smtplib
import time

#Just some various Constants
ADMIN = ["Admin","4846808235@txt.att.net","four"]
NO_MESSAGE = 'No new messages'

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
                      
                  else:
                      continue
    msgTuple = [varFrom, varBody] 
    mail.close()
    mail.logout()
    return(msgTuple)

#Sends a message
#IN: varTo = Address to send from, varMsg = Message to send
#OUT: Success or failure
def sendmsg(varTo, varMsg, verbose, varUser = 'jarvis104Mckee@gmail.com', varPass = 'jarvis104'):
    #Set variables
    to = varTo
    gmail_user = varUser
    gmail_pwd = varPass

    #Login
    smtpserver = smtplib.SMTP("smtp.gmail.com",587)
    smtpserver.ehlo()
    smtpserver.starttls()
    smtpserver.ehlo
    smtpserver.login(gmail_user, gmail_pwd)
    
    
    msg = "\r\n".join(["From: Jarvis","To: " + varTo,"A message From Jarvis","",varMsg,""])
    printmsg = "\r\n--->".join(["--->From: Jarvis","To: " + varTo,"A message From Jarvis","",varMsg,""])

    try:
        smtpserver.sendmail(gmail_user, to, msg.encode('utf-8'))
        if verbose > 0:
            print("-->Message sent:\n")
        if verbose > 1:
            print(printmsg)
    except SMTPException:
        print("SMTP Error")
    smtpserver.close()
    return

#                       --UserList Functions--
#   UserList Functions deal with the userList which exists in a file outside
#   of the program and needs to come inside. The userList is comprised of
#   userTuples with take the form:
#       userTuple = ["name","email/txt address","password"]
#   These userTuples are the primary form of security for the program.
#   Functions include:
#       -getUserList(verbose, source="users.jvs")
#       -textAll(userList, msg, verbose)
#       -changePass(userInfo, newPwd, quiet=False)
#       -addUser(userName, userAdd, userPwd, quiet=False)
#       -delUser(myUser, quiet=False)
#       -userBackup()
#       -exportUserList(source, userList)
#       -printUserList(userList)
#   Note: Maybe make user and userList into classes if you ever figure out
#   how to make classes in python
#

#Gets the user list from users.jvs
#IN: default(source=users.jvs)
#OUT: userList containing user tuples
def getUserList(verbose, source="users.jvs"):
    userList =[]
    if verbose > 0:
        print("-->Extracting userList from "+source+".")
    f = open(source)
    for i in f.readlines():
        list = i.replace("\n","")
        li = tuple(filter(None, list.split(';')))
        if verbose > 1:
            print("--->user " + li[0] + " added to userList.")
        userList.append(li)
    f.close()
    if verbose > 0:
        print("-->userList extracted from "+source+".")
    return(userList)

#Texts all members in a userList
#IN: userList, message = message to be sent
#OUT: None
def textAll(userList, msg, verbose):
    for user in userList:
        if verbose > 0:
            print("-->Message sent to "+user[0]+".\n")
        sendmsg(user[1], msg)
    return

#Changes a user's password
#IN: userInfo = user tuple, newPwd = string to be a password, quiet flag, verbose flag
#OUT: None
def changePass(userInfo, newPwd, verbose, quiet=False):
    userList = getUserList()
    for user in userList:
        if userInfo[0] == user[0]:
            delUser(user, verbose-1,True)
            addUser(user[0],user[1],newPwd, verbose-1,True)
            if verbose > 0:
                print("-->Password changed")
            break
    if not quiet:
        sendmsg(userInfo[1],"Password for " + userInfo[0] + " changed from "+ userInfo[2] + " to " +newPwd+".")
    return

#Adds a user based on input
#IN: userName, userAdd, userPwd, quiet flag, verbose flag (hopefully all the userXXX are self explanatory
#OUT: None
def addUser(userName, userAdd, userPwd, verbose, quiet=False):
    userList = getUserList(verbose)
    userList.append([userName,userAdd,userPwd])
    exportUserList("users.jvs", userList)
    if verbose > 0:
        print("-->User " + userName + " added.")
    if not quiet:
        sendmsg(myUser[1],"Hello! You have been added to my user list, "+myUser[0]+".")
        sendmsg(ADMIN[1],"User " + userInfo[0] + " added.")
    return

#Removes a user
#IN: myUser = userTuple, quiet flag, verbose flag
#OUT: None
def delUser(myUser, verbose, quiet=False):
    userList = getUserList(verbose)
    userList.remove(myUser)
    exportUserList("users.jvs", userList)
    if verbose > 0:
        print("-->User " + myUser[0] + " removed.")
    if not quiet:
        sendmsg(myUser[1],"You have been removed from my user list, "+myUser[0]+". Goodbye.")
        sendmsg(ADMIN[1],"User " + myUser[0] + " removed.")
    return

#Makes a userBackup to file backup.jvs
#IN: verbose flag
#OUT: None
def userBackup(verbose):
    if verbose > 0:
        print("-->Backing up...")
    x = getUserList(verbose)
    exportUserList("backup.jvs",x)
    if verbose > 0:
        print("-->userList backed up.")
    return

#Exports a userList to a specified source file
#IN: source = string with the sourcefile's name, userList to be stored
#OUT: None
def exportUserList(source, userList):
    file = open(source, "w")
    for i in userList:
        file.write(i[0]+";"+i[1]+";"+i[2]+"\n")
    return

#Prints the userList in the cmd window
#IN: verbose flag
#OUT: None
def printUserList(verbose):
    getUserList(verbose)
    print("User\t\tAddress\t\t\tPassword\n")
    for user in userList:
        print(user[0] + "\t\t" + user[1] + "\t\t\t" + user[2] + "\n")
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
    modeArray[0] = userMsg.count("-v")
    print("Verbose mode activated:\nVerbose Level " + str(modeArray[0]) +"\n")
    return(userMsg.replace('-v',''))

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
        sendmsg(prompt[0],prompt[1]+' SQUAWK')
    #rageParrotMode
    if modeArray[2] == True:
        sendmsg(prompt[0],"rageParrotMode is active but I'm not going to activate it yet. You're welcome.")
#        while i != 50:
#            i = i + 1
#            sendmsg(prompt[0],prompt[1]+' SQUAWK')
    return

#Sets up the default values for the modeArray
#IN: None
#OUT: modeArray
def getModeArrayDefaults():
    verbose = 2
    parrotMode = False
    rageParrotMode = False
    quiet = True
    modeArray = [verbose,parrotMode,rageParrotMode,quiet]
    return(modeArray)
    

