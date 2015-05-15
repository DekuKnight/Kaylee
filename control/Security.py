from dao.dao import dao
from bean.Message import Message
import re

class Security:

    @staticmethod
    def verify(message):
        d = dao()
        address = getattr(message,"sender")
        body = getattr(message,"body")
        
        query = d.query(("SELECT name,password FROM users where address=(?)",[address]))
        name,password = query.fetchone()
        if re.search(r'\b%s\b'%password,body,re.IGNORECASE) != None:
            print("\t%s sent a message!"%name)
            print("\t" + body)
            return True
        else:
            print("Invalid Password")
            return False