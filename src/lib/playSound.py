from functools import lru_cache
from queue import Queue
import threading
import time
import src.lib.Constants as CONSTANTS
import pygame

# def playSound(soundQueues):
#     soundPath = None
#     pygame.init()
#     pygame.mixer.init()
#     while True:
#         print("alive")
#         try:
#             soundPath = soundQueues.get(True,1)
#             print(soundPath)
#         except:
#             continue
#         if soundPath == "STOP" or soundPath =="":
#             break
#         pygame.mixer.find_channel().play(getSound(soundPath))
        
# @lru_cache(maxsize=32)
# def getSound(path):
#     sound = pygame.mixer.Sound(path)
#     sound.set_volume(0.2)
#     return sound
    

# if __name__ == "__main__":
#     queue = multiprocessing.Queue()
    
#     soundPlayProcess = multiprocessing.Process(target=playSound, args=(queue,))
#     soundPlayProcess.start()
#     for i in range(10):
#         queue.put("sound/bullet.wav")
#         time.sleep(0.5)
#     time.sleep(5)


import time
import random
import threading
from queue import Queue


# 自定义线程
class CustomThread(threading.Thread):
    def __init__(self, queue, **kwargs):
        super(CustomThread, self).__init__(**kwargs)
        self.__queue = queue
    def run(self):
        while True:
            item = self.__queue.get()
            item[0](*item[1:])
            self.__queue.task_done()

# 任务
def playSoundTask(soundPath):
    # thread_name = threading.current_thread().getName()
    # print('playing%s' % (soundPath))
    if soundPath == "":
        return
    sound = getSound(soundPath)
    if sound.__class__ == pygame.mixer.Sound:
        pygame.mixer.find_channel().play(sound)

@lru_cache(maxsize=32)
def getSound(path):
    sound = pygame.mixer.Sound(path)
    sound.set_volume(0.2)
    return sound

def initplaySound():
    # pygame.init()
    pygame.mixer.init()
    for i in range(5):
        t = CustomThread(CONSTANTS.playSoundPool, daemon=True)
        t.start()

def playSound(path):
    CONSTANTS.playSoundPool.put((playSoundTask, path))

# if __name__ == '__main__':
#     soungqueue=Queue()
#     poolqueue=Queue()
#     playSound(soungqueue,poolqueue)
#     for i in range(30):
#         time.sleep(0.1)
        
#         poolqueue.join()


    




'''
from functools import lru_cache
import multiprocessing
from queue import Queue
import threading
import time
# # import src.lib.Constants as CONSTANTS
import pygame

# def playSound(soundQueues):
#     soundPath = None
#     pygame.init()
#     pygame.mixer.init()
#     while True:
#         print("alive")
#         try:
#             soundPath = soundQueues.get(True,1)
#             print(soundPath)
#         except:
#             continue
#         if soundPath == "STOP" or soundPath =="":
#             break
#         pygame.mixer.find_channel().play(getSound(soundPath))
        
# @lru_cache(maxsize=32)
# def getSound(path):
#     sound = pygame.mixer.Sound(path)
#     sound.set_volume(0.2)
#     return sound
    

# if __name__ == "__main__":
#     queue = multiprocessing.Queue()
    
#     soundPlayProcess = multiprocessing.Process(target=playSound, args=(queue,))
#     soundPlayProcess.start()
#     for i in range(10):
#         queue.put("sound/bullet.wav")
#         time.sleep(0.5)
#     time.sleep(5)


import time
import random
import threading
from queue import Queue


# 自定义线程
class CustomThread(threading.Thread):
    def __init__(self, queue, **kwargs):
        super(CustomThread, self).__init__(**kwargs)
        self.__queue = queue
    def run(self):
        while True:
            item = self.__queue.get()
            item[0](*item[1:])
            self.__queue.task_done()

# 任务
def playSoundTask(soundPath):
    thread_name = threading.current_thread().getName()
    print('playing%s' % (thread_name))
    sound = getSound(soundPath)
    if sound.__class__ == pygame.mixer.Sound:
        pygame.mixer.find_channel().play(sound)

@lru_cache(maxsize=32)
def getSound(path):
    sound = pygame.mixer.Sound(path)
    sound.set_volume(0.2)
    return sound
def playSound(soundQueue):
    pygame.init()
    pygame.mixer.init()
    q = Queue()
    for i in range(10):
        t = CustomThread(q, daemon=True)
        t.start()
    while True:
        print("alive")
        try:
            soundPath = soundQueue.get(True,1)
            print(soundPath)
        except:
            continue
        if soundPath == "STOP" or soundPath =="":
            break
        q.put((playSoundTask, soundPath))
        q.join()

if __name__ == '__main__':
    soundQueue = multiprocessing.Queue()
    soundPlayProcess = multiprocessing.Process(target=playSound, args=(soundQueue,))
    soundPlayProcess.start()
    for i in range(10):
        time.sleep(0.1)
        soundQueue.put("sound/bullet.wav")

    
'''