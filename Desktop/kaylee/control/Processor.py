import re
from bean.Room import Room
from bean.Light import Light
from bean.Door import Door

class Processor:

    @staticmethod
    def process(msg,rooms):
        #for testing
        room = rooms[0]
        #Lights
        if re.search(r'lights',msg,re.IGNORECASE) != None:
            if re.search(r'on',msg,re.IGNORECASE) != None:
                for light in getattr(room,"lights"):
                    light.on()
            elif re.search(r'off',msg,re.IGNORECASE) != None:
                for light in getattr(room,"lights"):
                    light.off()
            else:
                for light in getattr(room,"lights"):
                    light.toggle()
        if re.search(r'lumos',msg,re.IGNORECASE) != None:
            for light in getattr(room,"lights"):
                    light.on()
        if re.search(r'nox',msg,re.IGNORECASE) != None:
            for light in getattr(room,"lights"):
                    light.off()
        #Doors
        if re.search(r'door',msg,re.IGNORECASE) != None:
            if re.search(r'\block\b',msg,re.IGNORECASE) != None:
                for door in getattr(room,"doors"):
                    door.lock()
            if re.search(r'\bunlock\b',msg,re.IGNORECASE) != None:
                for door in getattr(room,"doors"):
                    door.unlock()
            else:
                for door in getattr(room,"doors"):
                    door.toggle()
        if re.search(r'alohomora',msg,re.IGNORECASE) != None:
                for door in getattr(room,"doors"):
                    door.unlock()
