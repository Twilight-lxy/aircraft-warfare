class User:
    username = ""
    password = ""
    id = ""

    def __init__(self,username:str,password:str,id:str="") -> None:
        self.username = username
        self.password = password
        self.id = id
    
    def getUid(self):
        return self.id
    
    def setUid(self,id):
        self.id= id
    
    def getUname(self):
        return self.username
    
    def setUname(self,username):
        self.username = username
    
    def getUpassword(self):
        return self.password
    
    def setUname(self,password):
        self.password = password


class UserException(Exception):
    def __init__(self, info: str) -> None:
        super().__init__(self)
        self.errorinfo = info
    def __str__(self) -> str:
        return self.errorinfo

