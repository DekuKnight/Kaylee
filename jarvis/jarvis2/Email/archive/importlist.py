import imaplib
import email
import os
import smtplib

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

def sendmsg(varTo, varMsg, varUser = 'jarvis104Mckee@gmail.com', varPass = 'jarvis104'):
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
    
    
    msg = "\r\n".join(["From: Jarvis","To: " + varTo,"A message From Jarvis","",varMsg])
    try:
        smtpserver.sendmail(gmail_user, to, msg.encode('utf-8'))
        print('Message sent: \n' + msg)
    except SMTPException:
        print("SMTP Error")
    smtpserver.close()
    return

def getUserList():
    userList =[]
    f = open("users.txt")
    for i in f.readlines():
        list = i.replace("\n","")
        li = tuple(filter(None, list.split(';')))
        userList.append(li)
    f.close()
    return(userList)

def textAll(userList, msg):
    for user in userList:
        sendmsg(user[1], msg)
    return

def changePass(userInfo, newPwd):
    userList = getUserList()
    for user in userList:
        if userInfo[0] == user[0]:
            delUser(user)
            addUser(user[0],user[1],newPwd)
            print("password changed")
            break
    
    sendmsg(userInfo[1],"Password for " + userInfo[0] + " changed from "+ userInfo[2] + " to " +newPwd+".")
    return

def addUser(userName, userAdd, userPwd):
    userList = getUserList()
    userList.append([userName,userAdd,userPwd])
    exportUserList("users.txt", userList)
    print("User " + userName + " added.\n")
    return

def delUser(myUser):
    userList = getUserList()
    userList.remove(myUser)
    exportUserList("users.txt", userList)
    print("User " + myUser[0] + " deleted.\n")
    return

def exportUserList(source, userList):
    file = open(source, "w")
    for i in userList:
        file.write(i[0]+";"+i[1]+";"+i[2]+"\n")
    return

def printUserList(userList):
    print("User\t\tAddressP\t\t\tPassword\n")
    for user in userList:
        print(user[0] + "\t\t" + user[1] + "\t\t\t" + user[2] + "\n")
    return
