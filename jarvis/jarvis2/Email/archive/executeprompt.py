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

from functions import *

#executes the prompt described in newPrompt
#IN:  newPrompt variable, verbose flag
#OUT: Success flag if successful
def executePrompt(newPrompt, modeArray):
    returnFlag = CRAP

    if modeArray[0] > 0:
        print("-->Extracting Variables...\n")

    #Extract variables from prompt
    #
    varPrompt = newPrompt[1]
    varUser = getUser(newPrompt[0], modeArray[0])
            
    #Check if user is on the userList
    if varUser == FAILURE:
        print("User not found. Rejecting...\n")
        if modeArray[3] == True:
            sendmsg(varFrom, "You are not a user. You have been rejected.")
        return(FAILURE)
    
    if modeArray[0] > 0:
        print("-->User " + varUser[0] + " has sent a prompt.\n")
    if modeArray[0] > 1:
        print("--->Prompt sent: " + varPrompt + "\n")

#-------------------------editing stopped here---------------------------

    #Split up the prompt into separate words(units)
    units = varPrompt.split()
    
    #units will typically work as follows:
    # <password> <command> <additional parameters>

    #compile additional parameters into a list
    paramList = [units[2]]
    if paramList == None:
        for unit in units[3:]:
            paramList.append(unit)
            
    #check if the password is a valid password
    if varUser[2] == None:
        if modeArray[0] > 0:
            print("--No Password Provided\n")
        if modeArray[3] == True:
            sendmsg(varFrom, "No Password Provided")
        return(FAILURE)
    
    if units[0] != varUser[2]: #password is not the same
        if modeArray[0] > 0:
            print("--Wrong Password Sucker\n")
        if modeArray[3] == True:
            sendmsg(varFrom, "Wrong password moron!")
        return(FAILURE)

    #execute command
    if units[1] == "changePass":
        changePass(varUser, units[2])
    #return(execute(units[1],paramList))
    
    return CRAP

