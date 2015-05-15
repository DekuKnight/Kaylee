from functions import *
from executeprompt import *
import time

#modeArray Defaults
verbose = 2
parrotMode = False
rageParrotMode = False
quiet = True
modeArray = [verbose,parrotMode,rageParrotMode,quiet]

NO_MESSAGE = 'No new messages'

try:
    print('Hello sir.\n')
    while True:
        time.sleep(5)
        newPrompt = getprompt()

        #if there's a message send it through the works
        if newPrompt != NO_MESSAGE:

            #Toggle ParrotMode
            newPrompt[1] = toggleParrotMode(newPrompt[1], modeArray)

            #parrot
            if parrotMode == True:
                sendmsg(newPrompt[0], newPrompt[1] + ' SQUAWK')

            #verbose flag
            newPrompt[1] = verboseCount(newPrompt[1],modeArray)

            #quiet flag

            #if there is something execute the prompt
            result = executePrompt(newPrompt, modeArray)
            print(str(result) + "\n---------------------------------------\n\n")
                                
except KeyboardInterrupt:
    print('Goodbye Sir!')
    time.sleep(2)
