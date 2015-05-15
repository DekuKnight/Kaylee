from execute import *
from classes import *

cmd = "lightson"
ttuple = []

promptTuple = [cmd, ttuple]
tempUser = User("Ryan","4846808235@txt.att.net","X",0)
tempModeArray = [3,False,False,False]

result = execute(promptTuple,tempUser,tempModeArray)

print(promptTuple)

print("\n")

dbManager.printDB()

