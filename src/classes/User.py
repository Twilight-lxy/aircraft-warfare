class User:
    username = ""
    password = ""
    id = ""
    newpassword = ""

    def __init__(self,username:str,password:str,id:str) -> None:
        self.username = username
        self.password = password
        self.id = id
    
    @property
    def getUid(self):
        return self._id
    
    @id.setter
    def setUid(self,id):
        self._id= id
    
    @property
    def getUname(self):
        return self._username
    
    @username.setter
    def setUname(self,username):
        self._username = username
    
    @property
    def getUpassword(self):
        return self._password
    
    @password.setter
    def setUname(self,password):
        self._password = password

    @property
    def getUnewpassword(self):
        return self._newpassword
    
    @newpassword.setter
    def setUewpassword(self,newpassword):
        self._newpassword = newpassword

class UserException(Exception):
    def __init__(self, info: str) -> None:
        super().__init__(self)
        self.errorinfo = info
    def __str__(self) -> str:
        return self.errorinfo

