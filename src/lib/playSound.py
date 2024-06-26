from functools import lru_cache
import threading
import src.lib.Constants as CONSTANTS
import pygame
import threading


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
    if soundPath == "":
        return
    sound = getSound(soundPath)
    if sound.__class__ == pygame.mixer.Sound:
        try:
            pygame.mixer.find_channel().play(sound)
        except:
            pass


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
