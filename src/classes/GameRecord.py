class GameRecord:
    user=str
    time=str
    score=int
    def __init__() -> None:
        pass

class GameRecordException(Exception):
    def __init__(self, info: str) -> None:
        super().__init__(self)
        self.errorinfo = info
    def __str__(self) -> str:
        return self.errorinfo

