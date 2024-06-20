from concurrent.futures import thread
import threading
from queue import Queue
import time
import pygame
from src.lib.Constants import WINDOWS_SIZE, WIDTH, WHITE, RED, FPS
import src.lib.LoadResource
import traceback
import src.lib.Logo
import src.lib.textBox
from src.classes.ResourceDict import ResourceDict, AllResourceDict
import src.lib.LoginAndRegester
import src.lib.MainPage
import src.enitiy.hero
import src.lib.MainGame
def initGame():
    global screen
    pygame.init()
    pygame.mixer.init()
    screen = pygame.display.set_mode(WINDOWS_SIZE)
    pygame.display.set_caption("飞机大战")
    loadResourceThreading = threading.Thread(
        target=loadresource, name="loadresource", args=("loadresource", threadQueue)
    )
    loadResourceThreading.daemon = True
    loadResourceThreading.start()
    mess, per = ("load", "0")
    while not threadQueue.empty():
        threadQueue.get()
    while True:
        screen.fill(WHITE)
        src.lib.Logo.showLogo(screen)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
        if mess == "loaded":
            src.lib.textBox.draw_text_box(
                screen,
                mess="loading is complete!",
                fontSize=25,
                textBoxHeight=50,
                textBoxWidth=300,
                textBoxMidY=500,
                textBoxMidX=WIDTH / 2,
            )
            pygame.display.flip()
            break
        else:
            src.lib.textBox.draw_text_box(
                screen,
                mess="loading..." + per + "%",
                fontSize=25,
                textBoxHeight=50,
                textBoxWidth=200,
                textBoxMidY=500,
                textBoxMidX=WIDTH / 2,
            )
        pygame.display.flip()
        (mess, per) = threadQueue.get(True, 20)
    loadResourceThreading.join()
    pygame.mixer.music.play()
    time.sleep(1)
    screen.fill(WHITE)
    src.lib.Logo.showLogo(screen)
    pygame.display.flip()


def loadresource(name: str, queue: Queue):
    global soundResourceDict
    global resourceDict
    resourceDict = ResourceDict()
    queue.put(("loading", "0"))
    pygame.mixer.music.load("sound/game_music.ogg")
    pygame.mixer.music.set_volume(0.2)
    queue.put(("loading", "10"))
    background = pygame.image.load("images/background.png").convert()
    resourceDict.addResourse("hero",src.enitiy.hero.loadHeroAllResource())
    queue.put(("loading", "20"))
    soundResourceDict = src.lib.LoadResource.loadSoundResource()
    queue.put(("loading", "100"))
    queue.put(("loaded", "100"))


def logIn() -> str:
    global screen
    global threadQueue
    global mainClock
    while not threadQueue.empty():
        threadQueue.get()
    mess, username = ("login", "null")
    mouseInloginTextBox = False
    mouseInQuitTextBox = False
    while True:
        screen.fill(WHITE)
        src.lib.Logo.showLogo(screen, 0, 100)
        loginTextBox = src.lib.textBox.draw_text_box(
            screen,
            mess="login or register",
            fontSize=25,
            textBoxHeight=50,
            textBoxWidth=300,
            textBoxMidY=450,
            textBoxMidX=WIDTH / 2,
        )
        quitTextBox = src.lib.textBox.draw_text_box(
            screen,
            mess="quit",
            fontSize=25,
            textBoxHeight=50,
            textBoxWidth=300,
            textBoxMidY=550,
            textBoxMidX=WIDTH / 2,
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
                    src.lib.LoginAndRegester.getLoginMess(threadQueue)
                if mouseInQuitTextBox:
                    pygame.quit()
                    break
        if mess == "logined":
            break
        if mouseInloginTextBox:
            loginTextBox = src.lib.textBox.draw_text_box(
                screen,
                mess="login or register",
                fontSize=25,
                textBoxHeight=50,
                textBoxWidth=300,
                textBoxMidY=450,
                textBoxMidX=WIDTH / 2,
                textColor=WHITE,
                textBoxSideWidth=0,
            )
        if mouseInQuitTextBox:
            loginTextBox = src.lib.textBox.draw_text_box(
                screen,
                mess="quit",
                fontSize=25,
                textBoxHeight=50,
                textBoxWidth=300,
                textBoxMidY=550,
                textBoxMidX=WIDTH / 2,
                textColor=WHITE,
                textBoxSideWidth=0,
            )
        try:
            (mess, username) = threadQueue.get(False)
        except:
            pass
        pygame.display.flip()
        mainClock.tick(FPS)
    return username


def main():
    global screen
    global soundResourceDict
    global threadQueue
    global mainClock
    global resourceDict
    mainClock = pygame.time.Clock()
    threadQueue = Queue()
    initGame()
    src.lib.Logo.movingLogoFromTo(screen)
    while True:
        username = logIn()
        retmess = src.lib.MainPage.mainPage(screen, mainClock, username)
        if retmess == "start":
            src.lib.MainGame.startGame(screen,resourceDict,mainClock,username)
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
