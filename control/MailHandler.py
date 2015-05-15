import email
import imaplib
import re
import string
import smtplib
from bean.Message import Message

class MailHandler:

    mail = None
    smtpserver = None
    username = ""
    password = ""

    def __init__(self, username = 'jarvis104Mckee@gmail.com', password = 'kaylee104'):
        self.username = username
        self.password = password 
        self.mail = imaplib.IMAP4_SSL('imap.gmail.com')
        self.mail.login(self.username,self.password)
        try:
            self.smtpserver = smtplib.SMTP("smtp.gmail.com",587)
            self.smtpserver.ehlo()
            self.smtpserver.starttls()
            self.smtpserver.ehlo()
            self.smtpserver.login(self.username, self.password)
        except smtplib.SMTPException as e:
            print("Something went wrong with connecting to the server")
            print(e)

    def getMail(self,isSeen=False):
        newMessages = []
        status, msgs = self.mail.select('Inbox')

        if status != "OK":
            print("Fetching failed")
            return

        if isSeen:
            seen = "Seen"
        else:
            seen = "UnSeen"
            
        resp, data = self.mail.search(None, seen)

        nullMsg = data[0].decode('utf-8')
        if nullMsg == '':
            #print('No new messages')
            return []
    
        msg = []
        for msgNo in data[0].split():
            resp, message = self.mail.fetch(msgNo, '(RFC822)')
            msg.append(message)

        for element in msg:
            message = email.message_from_string(element[0][1].decode("utf-8"))
            varFrom = message['from']
            varDate = message['date']
              
            if message.get_content_type() == 'text/plain':
                       varBody = message.get_payload()

            for part in message.walk():
                  #For iphones? I think thats what this was?
                  if part.get_content_type() == 'text/html':
                      varBody = part.get_payload()
                      varBody = re.split('\W',varBody)
                      cnt = False
                      body = ''
                      for word in varBody:
                          if word == 'td':
                              cnt = not cnt
                          if cnt == True:
                              if word != 'td':
                                  body = " ".join([body,word])
                      varBody = body[1:]
                      
            m = Message([varFrom, varBody, varDate])
            newMessages.append(m)
        return newMessages

    def sendMail(self,user,msg):    
        message = "\r\n".join(["Kaylee Mainframe","","Message:","",str(msg),""])
        printmsg = "\r\n--->".join(["Kaylee Mainframe","","Message","",str(msg),""])

        try:
            self.smtpserver.sendmail(self.username, getattr(user,"address"),message.encode('utf-8'))
            print(printmsg)
        except smtplib.SMTPException as e:
            print("Something went wrong with sending a reply to %s" % getattr(user,"name"))
            print(e)
            
    def __del__(self):
        self.mail.close()
        self.smtpserver.quit()
        self.mail.logout()