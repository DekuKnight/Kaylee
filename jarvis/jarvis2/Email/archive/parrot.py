from mailhandlers import *
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
except KeyboardInterrupt:
    print('Goodbye Sir!')
