from functions import *

def execute(promptTuple, myUser, modeArray):
    #Split promptTuple up
    cmd, paramList = promptTuple

    try:
        #Admin Powers
        if myUser[1] == ADMIN[1]:
            #Text everyone!
            #paramList = <msg>
            if cmd == "textAll":
                textAll(getUserList(modeArray[0]),paramList[0],modeArray[0])
                return(SUCCESS)

            #In this case we can change another's password
            #paramList = <otherUser> <newPwd>
            elif cmd == "changePass":
                otherUser = getUserbyName(paramList[0],modeArray[0])
                if otherUser != FAILURE:
                    changePass(otherUser, paramList[1],modeArray[0],modeArray[3])
                    return(SUCCESS)
                #else: I'm changing my own password and it'll go down south
                    

            #Add a user
            #paramList = <otherName> <otherAdd> <otherPwd>
            elif cmd == "addUser":
                addUser(paramList[0],paramList[1],paramList[2],modeArray[0],modeArray[3])
                return(SUCCESS)

            #Delete a user
            #paramList = <otherName>
            elif cmd == "delUser":
                otherUser = getUserbyName(paramList[0],modeArray[0])
                if otherUser == FAILURE:
                    return(FAILURE)
                else:
                    delUser(otherUser,modeArray[0],modeArray[3])
                    return(SUCCESS)

            #Backup the userList
            #paramList = <>
            elif cmd == "userBackup":
                userBackup(modeArray[0])
                return(SUCCESS)
                
            #else: not an admin power and if it is not valid it'll get caught later
            

        #The rest of the mortals

        #Change your password
        #ParamList = <newPwd>
        if cmd == "changePass":
            changePass(myUser, paramList[0],modeArray[0],modeArray[3])
            return(SUCCESS)
        elif cmd == "lightsOn":
            lightsOn(modeArray[0])
            return(SUCCESS)
        elif cmd == "lightsOff":
            lightsOff(modeArray[0])
            return(SUCCESS)
        else:
            return([FAILURE,"Command does not exist"])
        
    except IndexError:
        return([FAILURE, "Prompt lacking parameters"])
