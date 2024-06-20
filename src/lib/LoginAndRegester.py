from queue import Queue
def getLoginMess(threadQueue:Queue) -> None:
    username = 'test'





    threadQueue.put(("logined",username))
    