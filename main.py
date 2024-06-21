from concurrent.futures import thread
import threading
from queue import Queue
import time
import pygame
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


def initGame():
    CONSTANTS.mainClock = pygame.time.Clock()
    pygame.init()
    CONSTANTS.superResourceDict = ResourceDict()
    CONSTANTS.screen = pygame.display.set_mode(CONSTANTS.WINDOWS_SIZE)
    CONSTANTS.threadQueue = Queue()
    pygame.mixer.init()
    pygame.display.set_caption("飞机大战")
    loadResourceThreading = threading.Thread(target=loadresource, name="loadresource")
    loadResourceThreading.daemon = True
    loadResourceThreading.start()
    mess, per = ("load", "0")
    while not CONSTANTS.threadQueue.empty():
        CONSTANTS.threadQueue.get()
    while True:
        CONSTANTS.screen.fill(CONSTANTS.WHITE)
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
    pygame.mixer.music.play()
    time.sleep(1)
    CONSTANTS.screen.fill(CONSTANTS.WHITE)
    src.lib.Logo.showLogo()
    pygame.display.flip()


def loadresource():
    CONSTANTS.threadQueue.put(("loading", "0"))
    pygame.mixer.music.load("sound/game_music.ogg")
    pygame.mixer.music.set_volume(0.2)
    CONSTANTS.threadQueue.put(("loading", "10"))
    backgroundImage = pygame.image.load("images/background.png").convert()
    CONSTANTS.superResourceDict.addResourse(
        CONSTANTS.HEROAIRCRAFT, Hero.loadHeroAllResource()
    )
    CONSTANTS.superResourceDict.addResourse(
        CONSTANTS.NORMALBULLET, NormalBullet.loadNormalBulletAllResource()
    )
    CONSTANTS.threadQueue.put(("loading", "20"))
    soundResourceDict = src.lib.LoadResource.loadSoundResource()
    CONSTANTS.threadQueue.put(("loading", "100"))
    CONSTANTS.threadQueue.put(("loaded", "100"))


def logIn() -> str:
    while not CONSTANTS.threadQueue.empty():
        CONSTANTS.threadQueue.get()
    mess, username = ("logined", "null")
    mouseInloginTextBox = False
    mouseInQuitTextBox = False
    while True:
        CONSTANTS.screen.fill(CONSTANTS.WHITE)
        src.lib.Logo.showLogo(0, 100)
        loginTextBox = src.lib.textBox.draw_text_box(
            mess="login or register",
            fontSize=25,
            textBoxHeight=50,
            textBoxWidth=300,
            textBoxMidY=450,
            textBoxMidX=CONSTANTS.WIDTH / 2,
        )
        quitTextBox = src.lib.textBox.draw_text_box(
            mess="quit",
            fontSize=25,
            textBoxHeight=50,
            textBoxWidth=300,
            textBoxMidY=550,
            textBoxMidX=CONSTANTS.WIDTH / 2,
        )
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                break
            if event.type == pygame.MOUSEMOTION:
                mouse_position = pygame.mouse.get_pos()
                if loginTextBox.collidepoint(mouse_position):
                    mouseInloginTextBox = True
                else:
                    mouseInloginTextBox = False
                if quitTextBox.collidepoint(mouse_position):
                    mouseInQuitTextBox = True
                else:
                    mouseInQuitTextBox = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if mouseInloginTextBox:
                    src.lib.LoginAndRegester.getLoginMess(CONSTANTS.threadQueue)
                if mouseInQuitTextBox:
                    pygame.quit()
                    break
        if mess == "logined":
            break
        if mouseInloginTextBox:
            loginTextBox = src.lib.textBox.draw_text_box(
                mess="login or register",
                fontSize=25,
                textBoxHeight=50,
                textBoxWidth=300,
                textBoxMidY=450,
                textBoxMidX=CONSTANTS.WIDTH / 2,
                textColor=CONSTANTS.WHITE,
                textBoxSideWidth=0,
            )
        if mouseInQuitTextBox:
            loginTextBox = src.lib.textBox.draw_text_box(
                mess="quit",
                fontSize=25,
                textBoxHeight=50,
                textBoxWidth=300,
                textBoxMidY=550,
                textBoxMidX=CONSTANTS.WIDTH / 2,
                textColor=CONSTANTS.WHITE,
                textBoxSideWidth=0,
            )
        try:
            (mess, username) = CONSTANTS.threadQueue.get(False)
        except:
            pass
        pygame.display.flip()
        CONSTANTS.mainClock.tick(CONSTANTS.FPS)
    return username


def main():
    initGame()
    src.lib.Logo.movingLogoFromTo()
    while True:
        username = logIn()
        retmess = src.lib.MainPage.mainPage(username)
        if retmess == "start":
            src.lib.MainGame.startGame(username)
        elif retmess == "ranking":
            pass  # showRankingList()
        elif retmess == "back":
            pass
        else:
            continue
        for event in pygame.event.get():  # 获取用户事件
            if event.type == pygame.QUIT:  # 如果事件为关闭窗口
                # 退出pygame
                pygame.quit()
                break


if __name__ == "__main__":
    try:
        main()
    except pygame.error:
        print("GoodBye")
    except:
        traceback.print_exc()
        # input()
