from mailhandlers import *
from importlist import*
import time

try:
    print('Hello sir.')
    while True:
        time.sleep(5)
        newPrompt = getprompt()

        if newPrompt == 'No new messages':
            print('x ')
        else:
            sendmsg(newPrompt[0], 'Parrot Mode Activated: ' + newPrompt[1] + ' SQUAWK')
            myList = getUserList()
            promptMsg = newPrompt[1].split()
            if list[0] == "changePass":
                changePass(promptMsg[1], myList, promptMsg[2], promptMsg[3])
except KeyboardInterrupt:
    print('Goodbye Sir!')
