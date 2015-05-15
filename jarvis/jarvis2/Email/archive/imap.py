import imaplib
import email
import os

USER = 'jarvis104Mckee@gmail.com'
PASSWORD = 'jarvis104'

mail = imaplib.IMAP4_SSL('imap.gmail.com')
mail.login(USER,PASSWORD)

mail.select('Inbox')

resp, data = mail.search(None, 'UnSeen')

for num in (data[0].split()):
  resp, msg = mail.fetch(num, '(RFC822)')
  
  #stuff is the string that contains the message
  #xyz is an message type that is coming from stuff
  #xyz = email.message_from_string(stuff)

  for response_part in msg:
      if isinstance(response_part, tuple):
          message = email.message_from_bytes(response_part[1])
          varSubject = message['subject']
          varFrom = message['from']

          if message.get_content_maintype() == 'multipart':
            print('Work that out later')
          else:
            for part in message.walk():
              if part.get_content_type() == 'text/plain':
                varBody = part.get_payload(decode=True)
              else:
                continue

  #remove the brackets around the sender email address
  varFrom = varFrom.replace('<', '')
  varFrom = varFrom.replace('>', '')

  #decode the body and make it pretty
  varBody = varBody.decode('utf-8')
    #for ATT
  varBody = varBody.replace("\r\n--\r\n==================================================================\r\nThis mobile text message is brought to you by AT&T\r\n",'')

    #for VTEXT
  varBody = varBody.replace("\r\n",'')

  #Get the provider
  if varFrom[-11:] == "txt.att.net":
        varProvider = 'ATT'
        varNumber = varFrom[:-12]
  elif varFrom[-9:] == "vtext.com":
        varProvider = 'VTEXT'
        varNumber = varFrom[:-10]
  else:
    continue

  #msgTuple = [from, msg, number, provider]
  msgTuple = [varFrom, varBody, varNumber, varProvider]
    
  print("Message Start ----------------\n")
  print(msgTuple)
  print("\nMessage End-----------------\n")


mail.close()
mail.logout()
