class User:
    user=""
    password=""
    def __init__(username:str) -> None:
        pass

class UserException(Exception):
    def __init__(self, info: str) -> None:
        super().__init__(self)
        self.errorinfo = info
    def __str__(self) -> str:
        return self.errorinfo

