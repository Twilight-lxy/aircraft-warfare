class GameRecord:
    id=str
    username=str
    time=str
    score=int
    def __init__(self,username:str,score:int,time:str) -> None:
        self.username = username
        self.time = time
        self.score = score
    def getUsername(self):
        return self.username
    def setUsername(self,username):
        self.username = username
    def getUid(self):
        return self.id
    def getUid(self,id):
        self.id = id
    def getUtime(self):
        return self.time
    def setUtime(self,time):
        self.time = time
    def getUscore(self):
        return self.score
    def setUscore(self,score):
        self.score = score
    
class GameRecordException(Exception):
    def __init__(self, info: str) -> None:
        super().__init__(self)
        self.errorinfo = info
    def __str__(self) -> str:
        return self.errorinfo

