from concurrent.futures import thread
import multiprocessing
import threading
from queue import Queue
import time
import pygame
from src.lib.playSound import initplaySound, playSound
from src.enitiy.bigEnemy import BigEnemy
from src.enitiy.gunBullet import GunBullet
from src.enitiy.machingGun import MachingGun
from src.lib.changePassword import changePassword
from src.enitiy.smallEnemy import SmallEnemy
import src.lib.LoginPage
from src.enitiy.aircraftGun import AircraftGun
from src.enitiy.hero import Hero
from src.enitiy.normalBullet import NormalBullet
import src.lib.Constants as CONSTANTS
import src.lib.LoadResource
import traceback
import src.lib.Logo
import src.lib.textBox
from src.classes.ResourceDict import ResourceDict, AllResourceDict
import src.lib.LoginAndRegester
import src.lib.MainPage
import src.lib.MainGame
import src.lib.rankingList
import otherresource.Ranking_ui
from src.lib.rankingList import showRankingList
from multiprocessing import Process


def initGame():

    CONSTANTS.mainClock = pygame.time.Clock()
    pygame.init()
    CONSTANTS.superResourceDict = ResourceDict()
    CONSTANTS.screen = pygame.display.set_mode(CONSTANTS.WINDOWS_SIZE)
    CONSTANTS.threadQueue = Queue()
    pygame.mixer.init()
    pygame.display.set_caption("飞机大战")
    loadResourceThreading = threading.Thread(target=src.lib.LoadResource.loadresource, name="loadresource")
    loadResourceThreading.daemon = True
    loadResourceThreading.start()
    mess, per = ("load", "0")
    backgroundImage = pygame.image.load("images/background.png").convert()
    CONSTANTS.superResourceDict.addResourse(CONSTANTS.GAMEBGIMAGE,backgroundImage)
    backgroundImage = pygame.transform.scale(backgroundImage, CONSTANTS.WINDOWS_SIZE)
    CONSTANTS.superResourceDict.addResourse(CONSTANTS.BGIMAGE,backgroundImage)
    while not CONSTANTS.threadQueue.empty():
        CONSTANTS.threadQueue.get()
    while True:
        CONSTANTS.screen.fill(CONSTANTS.WHITE)
        CONSTANTS.screen.blit(CONSTANTS.superResourceDict.getResource(CONSTANTS.BGIMAGE), (0, 0))
        src.lib.Logo.showLogo()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
        if mess == "loaded":
            src.lib.textBox.draw_text_box(
                mess="loading is complete!",
                fontSize=25,
                textBoxHeight=50,
                textBoxWidth=300,
                textBoxMidY=500,
                textBoxMidX=CONSTANTS.WIDTH / 2,
            )
            pygame.display.flip()
            break
        else:
            src.lib.textBox.draw_text_box(
                mess="loading..." + per + "%",
                fontSize=25,
                textBoxHeight=50,
                textBoxWidth=200,
                textBoxMidY=500,
                textBoxMidX=CONSTANTS.WIDTH / 2,
            )
        pygame.display.flip()
        (mess, per) = CONSTANTS.threadQueue.get(True, 20)
    loadResourceThreading.join()
    CONSTANTS.playSoundPool=Queue()
    initplaySound()
    pygame.mixer.music.play()
    time.sleep(1)
    CONSTANTS.screen.fill(CONSTANTS.WHITE)
    src.lib.Logo.showLogo()
    pygame.display.flip()


def main():
    initGame()
    CONSTANTS.screen.fill(CONSTANTS.WHITE)
    src.lib.Logo.movingLogoFromTo()
    queue = multiprocessing.Queue()
    changequeue = multiprocessing.Queue()
    queue.put(("close"))
    global killaim
    killaim = []
    username = None
    retmess = ""
    
    # CONSTANTS.soundQueue = multiprocessing.Queue()
    # soundPlayProcess = Process(target=playSound, args=(CONSTANTS.soundQueue,))
    # soundPlayProcess.start()    
    # killaim.append(soundPlayProcess)

    while True:
        if username == None:
            username = src.lib.LoginPage.logIn()
        if retmess == "":
            retmess = src.lib.MainPage.mainPage(username,changequeue)
        if retmess == "start":
            username , iscontinue = src.lib.MainGame.startGame(username)
            if iscontinue == "continue":
                retmess = "start"
            else:
                retmess = ""
        elif retmess == "ranking":
            retmess = ""
            closemess = ""
            try:
                closemess = queue.get(False)
            except:
                pass
            if closemess == "close":
                p1 = Process(target=showRankingList, args=(queue,))
                p1.start()
                killaim.append(p1)
        elif retmess == "changePassword":
            closemess = ""
            try:
                closemess = queue.get(False)
            except:
                pass
            if closemess == "close":
                p2 = Process(target=changePassword, args=(username,queue,changequeue))
                p2.start()
                killaim.append(p2)
        elif retmess == "back":
            username = None
            retmess = ""
            pass
        else:
            continue
        for event in pygame.event.get():  # 获取用户事件a
            if event.type == pygame.QUIT:  # 如果事件为关闭窗口
                # 退出pygame
                pygame.quit()
                break


if __name__ == "__main__":
    global killaim
    killaim = None
    try:
        main()
    except pygame.error:
        for i in killaim:
            try:
                i.kill()
            except:
                pass
        print("GoodBye")
    except:
        traceback.print_exc()
        # input()
