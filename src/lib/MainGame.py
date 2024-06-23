from queue import Queue
import threading
import time
import pygame
from pygame import Surface
from src.lib.pauseWindow import pasueMain
from src.enitiy.smallEnemy import SmallEnemy
import src.lib.Constants as CONSTANTS
from src.classes.GameRecord import GameRecord
from src.classes.User import User
from src.classes.ResourceDict import ResourceDict
from src.enitiy.hero import Hero
from src.enitiy.normalBullet import NormalBullet
def startGame(username:User) -> GameRecord:
    gameRecord = GameRecord
    CONSTANTS.aircraftGroup = pygame.sprite.Group()
    CONSTANTS.weaponBulletGroup = pygame.sprite.Group()
    gamePause = False
    queue = Queue()
    mess = ""
    pygame.mixer.music.play(-1)
    CONSTANTS.screen.fill(CONSTANTS.WHITE)
    hero = Hero()
    # testbullet = NormalBullet(False,100,10)
    CONSTANTS.aircraftGroup.add(hero)
    # CONSTANTS.weaponBulletGroup.add(testbullet)
    CONSTANTS.aircraftGroup.add(SmallEnemy(200,20))
    while True:
        if(gamePause):
            try:
                mess = queue.get(True,0.2)
            except:
                pass
            if(mess == "continue"):
                mess = ""
                gamePause = False
            if(mess == "esc"):
                mess = ""
                gameover()
                break
            pygame.display.flip()
            CONSTANTS.mainClock.tick(CONSTANTS.FPS)
            pygame.event.pump()
            continue
        CONSTANTS.screen.fill(CONSTANTS.WHITE)
        CONSTANTS.aircraftGroup.update()
        CONSTANTS.weaponBulletGroup.update()
        for event in pygame.event.get():  # 获取用户事件
            if event.type == pygame.QUIT:  # 如果事件为关闭窗口
                # 退出pygame
                pygame.quit()
                break
        mess = ""
        mess = hero.moveByKeyboard(pygame.key.get_pressed())
        if(mess == "Pause"):
            gamePause = True
            while mess=="Pause":
                mess = hero.moveByKeyboard(pygame.key.get_pressed())
                pygame.event.pump()
            pauseThreading = threading.Thread(target=pasueMain, name="loadresource",args=(queue,))
            pauseThreading.daemon = True
            pauseThreading.start()
            
        if(mess == "GameOver"):
            gameContinue = False
        CONSTANTS.weaponBulletGroup.draw(CONSTANTS.screen)
        CONSTANTS.aircraftGroup.draw(CONSTANTS.screen)
        groupCollideAns=pygame.sprite.groupcollide(CONSTANTS.aircraftGroup,CONSTANTS.weaponBulletGroup,0,0)
        for hitFrom,hitlist in groupCollideAns.items():
            for hitaim in hitlist:
                doGroupCollode(hitFrom,hitaim)
        # print(testsmallenemy.allRes.getValue(CONSTANTS.HP))
        # test = NormalBullet(True,100,10)
        # test.setAutoMove(True,0,10)
        # CONSTANTS.weaponBulletGroup.add(test)

        pygame.display.flip()
        CONSTANTS.mainClock.tick(CONSTANTS.FPS)
        pygame.event.pump()

    return gameRecord
def gameover():
    pass

def doGroupCollode(aircraft,bullet):
    if bullet.deathing == -1:
        aircraft.hit(bullet)
    if aircraft.deathing == -1:
        bullet.hit(aircraft)