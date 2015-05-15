# Import smtplib for the actual sending function
import smtplib

to = '4846808235@txt.att.net'
gmail_user = 'jarvis104Mckee@gmail.com'
gmail_pwd = 'jarvis104'
smtpserver = smtplib.SMTP("smtp.gmail.com",587)
smtpserver.ehlo()
smtpserver.starttls()
smtpserver.ehlo
smtpserver.login(gmail_user, gmail_pwd)
header = 'To:' + to + '\n' + 'From: ' + gmail_user + '\n' + 'Subject:testing \n'
print(header)
msg = header + '\n Test\n\n'
smtpserver.sendmail(gmail_user, to, msg)
print('done')
smtpserver.close()

