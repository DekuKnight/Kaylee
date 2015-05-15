#----------------------------------------------------------------------
#||  Project Jarvis
#||  Version 2.0
#||
#||  Author:         Ryan Wright
#||  Email:          rdwright5127@gmail.com
#||  Last Modified:  12.6.13
#||
#||  File Description: jarvis.py
#||      This file is the main program where the rest of the program
#||     branches off from. A loop continually checks for new mail and
#||     Then executes the incoming prompt
#|| 

from functions import *
from execute import *

tempModeArray = getModeArrayDefaults()

try:
    print('Hello sir.\n')
    while True:
        time.sleep(5)
        newPrompt = getprompt()

        #if there's a message send it through the works
        if newPrompt != NO_MESSAGE:

            #Just say something so we know we got something
            print("----------------------------------------\n\tNew Message Recieved!\n----------------------------------------\n")

            #parrot
            parrot(newPrompt, tempModeArray)

            #Do security checks
            #if it fails promptTuple will be a string with the error message
            returns, promptTuple, myUser = conditionPrompt(newPrompt,tempModeArray)

            #if it is sucessful
            if returns == SUCCESS:
                #execute(promptTuple() = (command, parameter array), user, modeArray )
                result = execute(promptTuple,myUser,tempModeArray)
                print(result)
                                      
            else: #FAILURE
                print(promptTuple)
                if tempModeArray[3] == False:
                    sendmsg(myUser[1],promptTuple,tempModeArray[0])

            print("\n----------------------------------------\n\n")
                                
except KeyboardInterrupt:
    print('Goodbye Sir!')
    time.sleep(2)
