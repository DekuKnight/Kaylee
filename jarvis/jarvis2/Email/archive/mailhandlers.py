def getprompt():
    import imaplib
    import email
    import os

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
                      print("GARGLE\n")
                      varBody = varBody.decode('utf-8')
                      print(varBody + '\n')
                      head = varBody.find('<td>')
                      tail = varBody.rfind('</td>')
                      varBody = varBody[head+4:tail]
                      varBody = varBody.replace("\r\n","")
                      varBody = varBody.strip()
                      print(varBody)
                  else:
                      continue
                    
    msgTuple = [varFrom, varBody] 
    mail.close()
    mail.logout()
    return(msgTuple)

def sendmsg(varTo, varMsg, varUser = 'jarvis104Mckee@gmail.com', varPass = 'jarvis104'):
    # Import smtplib for the actual sending function
    import smtplib

    to = varTo
    gmail_user = varUser
    gmail_pwd = varPass
    smtpserver = smtplib.SMTP("smtp.gmail.com",587)
    smtpserver.ehlo()
    smtpserver.starttls()
    smtpserver.ehlo
    smtpserver.login(gmail_user, gmail_pwd)
    
    msg = "\r\n".join(["From: Jarvis","To: You","A message From Jarvis","",varMsg])
    try:
        smtpserver.sendmail(gmail_user, to, msg.encode('utf-8'))
        print('Message sent: \n' + msg)
    except SMTPException:
        print("SMTP Error")
    smtpserver.close()



