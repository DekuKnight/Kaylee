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
def conditionPrompt(newPrompt, modeArray):
    errormsg = "Somethin' strange happened!"

    #cleanup the prompt
    #Toggle ParrotMode
    newPrompt[1] = toggleParrotMode(newPrompt[1], modeArray)

    #Toggle RageParrotMode
    newPrompt[1] = toggleRageParrotMode(newPrompt[1], modeArray)

    #verbose flag
    newPrompt[1] = verboseCount(newPrompt[1],modeArray)

    #quiet flag
    
    if modeArray[0] > 0:
        print("-->Extracting Variables...\n")

    #Extract variables from prompt
    #
    varPrompt = newPrompt[1]
    varUser = getUser(newPrompt[0], modeArray[0])
            
    #Check if user is on the userList
    if varUser == FAILURE:
        errormsg = "User not found. Rejecting...\n"
        if modeArray[3] == False:
            sendmsg(varFrom, "You are not a user. You have been rejected.")
        return([FAILURE,errormsg])
    
    if modeArray[0] > 0:
        print("-->User " + varUser[0] + " has sent a prompt.\n")
    if modeArray[0] > 1:
        print("--->Prompt sent: " + varPrompt + "\n")

    #Split up the prompt into separate words(units)
    units = varPrompt.split()
    
    #units will typically work as follows:
    # <password> <command> <additional parameters>

    promptPass = None
    command = None
    paramList = []
    
    if len(units) >= 3:
        for unit in units[2:]:
            paramList.append(unit)
        command = units[1]
    elif len(units) >= 2:
        paramList.append("Empty")
        command = units[1]
    elif len(units) >= 1:
        promptPass = units[0]
    else:
        errormsg = "Empty prompt"
        return([FAILURE,errormsg])
            
    #check if the password is a valid password (OBSOLETE?)
    if varUser[2] == None:
        errormsg = "No Password Provided"
        if modeArray[3] == True:
            sendmsg(varUser[1], "No Password Provided", modeArray[0])
        return([FAILURE,errormsg])
    
    if units[0] != varUser[2]: #password is not the same
        errormsg = "Wrong Password Sucker"
        if modeArray[3] == False:
            sendmsg(varUser[1], "Wrong password!", modeArray[0])
        return([FAILURE,errormsg])

    #create responding tuple
    #   function status, promptTuple = [command, parameter array]
    resultTuple = [SUCCESS, [command,paramList]]
    
    return resultTuple

