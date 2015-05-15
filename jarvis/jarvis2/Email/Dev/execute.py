from classes import *

def execute(promptTuple, myUser, modeArray):
    #Split promptTuple up
    cmd, paramList = promptTuple
    cmd = cmd.upper()
    admin = User("Ryan","4846808235@txt.att.net","X",0)

    try:
        #Admin Powers
        if myUser.clearance == ADMIN:
            verbose(("Welcome Admin %s" %myUser.name),1,modeArray[0])
            #In this case we can change another's password
            #paramList = <otherUser> <newPwd>
            if cmd == "CHANGEPASS":
                otherUser = returnUser(paramList[0])
                if otherUser != FAILURE:
                    otherUser.changePwd(paramList[1])
                    verbose(("Password for User %s changed to %s" %(otherUser.name,otherUser.pwd)),2,modeArray[0])
                    speak("%s's password has changed to %s" %(otherUser.name,otherUser.pwd), myUser.add,modeArray)
                    speak("Your password has changed to %s" %otherUser.pwd, otherUser.add,modeArray)
                    return(SUCCESS)
                #else: I'm changing my own password and it'll go down south
                #unless my password is someone else's name then i'm in trouble
                    
            #Add an admin
            #paramList = <otherName> <otherAdd> <otherPwd>
            elif cmd == "ADDADMIN":
                addAdmin(paramList[0],paramList[1],paramList[2])
                verbose(("Admin %s added" %paramList[0]),2,modeArray[0])
                speak("Admin %s added" %paramList[0], myUser.add, modeArray)
                return(SUCCESS)

            #Delete a user
            #paramList = <otherName>
            elif cmd == "DELADMIN":
                otherUser = returnUser(paramList[0])
                if otherUser == FAILURE:
                    return([FAILURE,"Admin not found"])
                else:
                    delAdmin(otherUser.name)
                    verbose(("Admin %s deleted" %paramList[0]),2,modeArray[0])
                    speak("Admin %s deleted" %paramList[0], myUser.add, modeArray)
                    return(SUCCESS)

            #Add a user
            #paramList = <otherName> <otherAdd> <otherPwd>
            elif cmd == "ADDUSER":
                addUser(paramList[0],paramList[1],paramList[2])
                verbose(("User %s added" %paramList[0]),2,modeArray[0])
                speak("User %s added" %paramList[0], myUser.add, modeArray)
                return(SUCCESS)

            #Delete a user
            #paramList = <otherName>
            elif cmd == "DELUSER":
                otherUser = returnUser(paramList[0])
                if otherUser == FAILURE:
                    return([FAILURE,"User not found"])
                else:
                    delUser(otherUser.name)
                    verbose(("User %s deleted" %paramList[0]),2,modeArray[0])
                    speak("User %s deleted" %paramList[0], myUser.add, modeArray)
                    speak("You have been deleted from the Jarvis mainframe! Have a nice day!", otherUser.add,modeArray)
                    return(SUCCESS)

            #Add a temp
            #paramList = <otherName> <otherAdd>
            elif cmd == "ADDTEMP":
                addTemp(paramList[0],paramList[1])
                verbose(("Temporary User %s added" %paramList[0]),2,modeArray[0])
                speak("Temporary User %s added" %paramList[0], myUser.add, modeArray)
                speak("Welcome Temporary User %s! You have 30 minutes on the Jarvis mainframe before you are deleted. Spend it wisely!" %paramList[0], paramList[1], modeArray)
                return(SUCCESS)
                
            #else: not an admin power and if it is not valid it'll get caught later
            

        #The rest of the mortals

        #Users
        if myUser.clearance <= USER:
            #Change your password
            #ParamList = <newPwd>
            if cmd == "CHANGEPASS":
                myUser.changePwd(paramList[0])
                verbose(("User %s's password has been changed to %s" %(myUser.name,myUser.pwd)),2,modeArray[0])
                speak("Your password has been changed to %s", myUser.add,modeArray)
                return(SUCCESS)

            elif ((cmd == "LIGHTSON") or (cmd == "LUMOS")):
                print("Lights ON...")
                #lightsOn()
                verbose(("User %s turned the lights on" %myUser.name),2,modeArray[0])
                speak("Lights are on", myUser.add, modeArray)
                return(SUCCESS)
            
            elif ((cmd == "LIGHTSOFF")or(cmd == "NOX")):
                print("Lights OFF...")
                #lightsOff()
                verbose(("User %s turned the lights off" %myUser.name),2,modeArray[0])
                speak("Lights are off", myUser.add, modeArray)
                return(SUCCESS)

        if myUser.clearance <= TEMP:
            if cmd == "LOCK":
                print("Door Locked...")
                #lockDoor()
                verbose(("User %s locked the door" %myUser.name),2,modeArray[0])
                speak("Door locked", myUser.add, modeArray)
                return(SUCCESS)

            elif ((cmd == "UNLOCK")or(cmd == "ALOHOMORA")):
                print("Door Unlocked...")
                #unlockDoor()
                verbose(("User %s unlocked the door" %myUser.name),2,modeArray[0])
                sendmsg(admin.add,"Door locked by %s" %myUser.name,modeArray[0])
                speak("Door unlocked", myUser.add, modeArray)
                return(SUCCESS)
            
        else:
            return([FAILURE,"Command does not exist"])
        
    except IndexError:
        return([FAILURE, "Prompt lacking parameters"])

#Testing

