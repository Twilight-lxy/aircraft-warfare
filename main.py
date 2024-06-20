from concurrent.futures import thread
import threading
from queue import Queue
import time
import pygame
from src.lib.Constants import WINDOWS_SIZE, WIDTH, WHITE, RED
import src.lib.LoadResource
import traceback
import src.lib.Logo
import src.lib.textBox
from src.classes.ResourceDict import ResourceDict


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
    queue.put(("loading", "0"))
    pygame.mixer.music.load("sound/game_music.ogg")
    pygame.mixer.music.set_volume(0.2)
    queue.put(("loading", "10"))
    background = pygame.image.load("images/background.png").convert()
    queue.put(("loading", "20"))
    soundResourceDict = src.lib.LoadResource.loadSoundResource()
    queue.put(("loading", "100"))
    queue.put(("loaded", "100"))


def logIn():
    global screen
    global threadQueue
    global mainClock
    src.lib.Logo.movingLogoFromTo(screen)
    while not threadQueue.empty():
        threadQueue.get()
    mess, username = ("login", "null")
    mouseInloginTextBox = False
    mouseInloginQuitBox = False
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
                    mouseInloginQuitBox = True
                else:
                    mouseInloginQuitBox = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if mouseInloginTextBox:
                    pass  # getLoginMess(threadQueue)
                if mouseInloginQuitBox:
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
        if mouseInloginQuitBox:
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
            (mess, per) = threadQueue.get(False)
        except:
            pass
        pygame.display.flip()
        mainClock.tick(60)


def main():
    global screen
    global soundResourceDict
    global threadQueue
    global mainClock
    mainClock = pygame.time.Clock()
    threadQueue = Queue()
    initGame()
    logIn()
    while True:
        for event in pygame.event.get():  # 获取用户事件
            if event.type == pygame.QUIT:  # 如果事件为关闭窗口
                # 退出pygame
                pygame.quit()
                break
            elif event.type == pygame.MOUSEBUTTONDOWN:
                pygame.mouse.get_pos()


if __name__ == "__main__":
    try:
        main()
    except SystemExit:
        pass
    except:
        traceback.print_exc()
        pygame.quit()
        # input()
