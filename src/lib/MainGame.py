from queue import Queue
import random
import threading
import time
import pygame
from pygame import Surface
from src.enitiy.addFuelBullet import AddFuelBullet
from src.enitiy.addBulletBullet import AddBulletBullet
from src.lib.gameoverWindow import gameoverWindow
from src.enitiy.missile import Missile
from src.enitiy.middleEnemy import MiddleEnemy
from src.enitiy.addHpBullet import AddHpBullet
from src.lib.DataBaseFunc import addToRankingList
from src.enitiy.bigEnemy import BigEnemy
from src.lib.pauseWindow import pasueMain
from src.enitiy.smallEnemy import SmallEnemy
import src.lib.Constants as CONSTANTS
from src.classes.GameRecord import GameRecord
from src.classes.User import User
from src.classes.ResourceDict import ResourceDict
from src.enitiy.hero import Hero
from src.enitiy.normalBullet import NormalBullet
from src.lib.textBox import draw_text_box
from src.lib.healthBar import drawHealthBar


def startGame(username: User):
    heroScore = 0
    gameRecord = GameRecord
    CONSTANTS.allEnemyGroup = pygame.sprite.Group()
    gamePause = False
    pauseQueue = Queue()
    addMessQueue = Queue()
    mess = ""
    pygame.mixer.music.play(-1)
    CONSTANTS.screen.fill(CONSTANTS.WHITE)
    CONSTANTS.screen.blit(CONSTANTS.superResourceDict.getResource(CONSTANTS.BGIMAGE), (0, 0))
    hero = Hero()
    CONSTANTS.hero = hero
    CONSTANTS.allEnemyGroup.add(hero)
    addEnemyThread = threading.Thread(
        target=addEnemy, name="addEnemy", args=(addMessQueue, CONSTANTS.allEnemyGroup)
    )
    addEnemyThread.daemon = True
    addEnemyThread.start()
    while True:
        if gamePause:
            try:
                mess = pauseQueue.get(True, 0.2)
            except:
                pass
            if mess == "continue":
                mess = ""
                gamePause = False
            if mess == "esc":
                mess = ""
                addMessQueue.put("STOP")
                addEnemyThread.join()
                addToRankingList(GameRecord(username, heroScore, ""))
                if hero.HP <= 0:
                    overMessQueue = Queue()
                    gameoverWindow(heroScore, overMessQueue)
                    overMess = ""
                    try:
                        overMess = overMessQueue.get()
                    except:
                        pass
                    if overMess == "continue":
                        return (username, "continue")
                # 显示游戏结束界面，显示分数，一个按钮，返回主界面

                return (username, "esc")
            pygame.display.flip()
            CONSTANTS.mainClock.tick(CONSTANTS.FPS)
            pygame.event.pump()
            continue
        CONSTANTS.screen.fill(CONSTANTS.WHITE)
        CONSTANTS.screen.blit(CONSTANTS.superResourceDict.getResource(CONSTANTS.BGIMAGE), (0, 0))
        CONSTANTS.allEnemyGroup.update()
        for event in pygame.event.get():  # 获取用户事件
            if event.type == pygame.QUIT:  # 如果事件为关闭窗口
                # 退出pygame
                gamePause = True
                mess = "esc"
                break
        keymess = ""
        keymess = hero.moveByKeyboard(pygame.key.get_pressed())
        if keymess == "Pause":
            gamePause = True
            while keymess == "Pause":
                keymess = hero.moveByKeyboard(pygame.key.get_pressed())
                pygame.event.pump()
            pauseThreading = threading.Thread(
                target=pasueMain, name="pasueMain", args=(pauseQueue,)
            )
            pauseThreading.daemon = True
            pauseThreading.start()
            addMessQueue.put(pauseThreading)
        if keymess == "GameOver":
            gamePause = True
            mess = "esc"
        try:
            CONSTANTS.allEnemyGroup.draw(CONSTANTS.screen)
        except:
            print("draw error!")
        groupCollideAns = pygame.sprite.groupcollide(
            CONSTANTS.allEnemyGroup, CONSTANTS.allEnemyGroup, 0, 0
        )
        for hitFrom, hitlist in groupCollideAns.items():
            for hitaim in hitlist:
                heroScore += doGroupCollide(hitFrom, hitaim)
        updateUI(heroScore, hero)
        pygame.display.flip()
        CONSTANTS.mainClock.tick(CONSTANTS.FPS)
        pygame.event.pump()

    return ""


def doGroupCollide(aim1, aim2):
    if aim1.iFF == aim2.iFF:
        return 0
    if not collideMask(aim1.mask, aim2.mask, (aim1.X, aim1.Y), (aim2.X, aim2.Y)):
        return 0
    if aim1 == aim2:
        return 0
    aim1hitaim2 = False
    aim2hitaim1 = False
    if aim1.HP > 0:
        aim1hitaim2 = True
    if aim2.HP > 0:
        aim2hitaim1 = True
    if aim1hitaim2:
        if aim1.TYPE == CONSTANTS.BulletType and aim2.canBeBullet == False:
            pass
        else:
            aim1.hit(aim2)
    if aim2hitaim1:
        if aim1.canBeBullet == False and aim2.TYPE == CONSTANTS.BulletType:
            pass
        else:
            aim2.hit(aim1)
    if aim1.HP <= 0 and aim1.deathing == -1:
        addScore = aim1.killScore
        if addScore != -1:
            return addScore
    return 0


def collideMask(mask1, mask2, pos1, pos2):  # 用于检测Mask碰撞的函数
    return mask1.overlap(mask2, (pos2[0] - pos1[0], pos2[1] - pos1[1]))


def addEnemy(queue: Queue, airGroup):
    lastAddSmallEnemyTime = 0
    lastAddMiddleEnemyTime = 0
    lastAddBigEnemyTime = 0

    lastAddBUlletBulletTime = 0
    lastAddFuelBulletTime = 0
    lastAddAddHpBulletTime = 0
    while True:
        time.sleep(0.5)
        mess = None
        nowTime = pygame.time.get_ticks()
        try:
            mess = queue.get(False)
        except:
            pass
        if mess == "STOP":
            break
        elif mess != None:
            try:
                mess.join()
            except:
                pass
        if len(airGroup.sprites()) > 100:
            time.sleep(0.5)
            continue
        if nowTime > 1000 and nowTime - lastAddSmallEnemyTime > 1000:
            random.seed()
            if random.randint(1, 100) > 20:
                addEnemyWithoutCollide(airGroup,SmallEnemy(random.randint(20, CONSTANTS.WIDTH), 20))
            lastAddSmallEnemyTime = nowTime
        if nowTime > 6000 and  nowTime - lastAddMiddleEnemyTime > 2000:
            random.seed()
            if random.randint(1, 100) > 50:
                addEnemyWithoutCollide(airGroup,MiddleEnemy(random.randint(20, CONSTANTS.WIDTH), 20))
            lastAddMiddleEnemyTime = nowTime
        if  nowTime > 15000 and nowTime - lastAddBigEnemyTime > 2000:
            random.seed()
            if random.randint(1, 100) > 75:
                addEnemyWithoutCollide(airGroup,BigEnemy(random.randint(20, CONSTANTS.WIDTH), 20))
            lastAddBigEnemyTime = nowTime
        
        if nowTime > 20000 and nowTime - lastAddAddHpBulletTime > 10000:
            random.seed()
            if random.randint(1, 100) > 90:
                addEnemyWithoutCollide(airGroup,AddHpBullet(False, random.randint(20, CONSTANTS.WIDTH), 0))
            lastAddAddHpBulletTime = nowTime
        if nowTime > 20000 and nowTime - lastAddBUlletBulletTime > 10000:
            random.seed()
            if random.randint(1, 100) > 50:
                addEnemyWithoutCollide(airGroup,AddBulletBullet(False, random.randint(20, CONSTANTS.WIDTH), 0))
            lastAddBUlletBulletTime = nowTime
        if nowTime > 20000 and nowTime - lastAddFuelBulletTime > 10000:
            random.seed()
            if random.randint(1, 100) > 75:
                addEnemyWithoutCollide(airGroup,AddFuelBullet(False, random.randint(20, CONSTANTS.WIDTH), 0))
            lastAddFuelBulletTime = nowTime

def addEnemyWithoutCollide(airGroup,addAim):
    groupCollideAns = pygame.sprite.spritecollide(
        addAim,
        airGroup,
        0,
    )
    if len(groupCollideAns) != 0:
        for i in groupCollideAns:
            if collideMask(addAim.mask, i.mask, (addAim.X, addAim.Y), (i.X, i.Y)):
                return False
    airGroup.add(addAim)
    return True
    

def updateUI(heroScore, hero: Hero):
    draw_text_box(
        fontSize=20,
        mess="    Score:  " + str(heroScore) + "    ",
        textBoxMidX=CONSTANTS.WIDTH - 50,
        textBoxMidY=10,
        textBoxWidth=10,
        textBoxHeight=40,
    )
    # pygame.draw.rect(
    #     CONSTANTS.screen,
    #     CONSTANTS.WHITE,
    #     (0, CONSTANTS.HEIGHT, CONSTANTS.WIDTH, CONSTANTS.UIHEIGHT),
    # )
    pygame.draw.rect(
        CONSTANTS.screen, CONSTANTS.BLACK, (0, CONSTANTS.HEIGHT, CONSTANTS.WIDTH, 1)
    )
    drawHealthBar(
        16,
        CONSTANTS.HEIGHT + 1,
        100,
        40,
        hero.fullHp,
        hero.HP,
    )
    draw_text_box(
        fontSize=15,
        mess=" HP: " + str(hero.HP),
        textBoxMidX=66,
        textBoxMidY=CONSTANTS.HEIGHT + 21,
        textBoxWidth=100,
        textBoxHeight=40,
        autoWidth=False,
        autoHeight=False,
    )
    drawHealthBar(
        16,
        CONSTANTS.HEIGHT + 42,
        100,
        40,
        hero.fullfuel,
        hero.fuel,
        color_full=CONSTANTS.BLUE,
    )
    draw_text_box(
        fontSize=15,
        mess=" FUEL: " + str(hero.fuel),
        textBoxMidX=66,
        textBoxMidY=CONSTANTS.HEIGHT + 62,
        textBoxWidth=100,
        textBoxHeight=40,
        autoWidth=False,
        autoHeight=False,
    )

    info = hero.weaponState()
    mess = None
    if info[2] <= 0:
        mess = ("EMPTY", CONSTANTS.RED, 0)
    elif pygame.time.get_ticks() - info[4] < 10:
        mess = ("FIRE", CONSTANTS.BLUE, 0)
    elif pygame.time.get_ticks() - info[4] < info[5]:
        mess = ("Loading", CONSTANTS.RED, 1)
    else:
        mess = ("StandBy", CONSTANTS.GREEN, 0)
    if mess[0] == "Loading":
        drawHealthBar(
            16,
            CONSTANTS.HEIGHT + 82,
            100,
            40,
            info[5],
            pygame.time.get_ticks() - info[4],
            color_full=CONSTANTS.RED,
        )

    draw_text_box(
        fontSize=15,
        mess=mess[0],
        textBoxMidX=66,
        textBoxMidY=CONSTANTS.HEIGHT + 103,
        textBoxWidth=100,
        textBoxHeight=40,
        autoWidth=False,
        autoHeight=False,
        textBoxColor=mess[1],
        textBoxSideWidth=mess[2],
    )

    info = hero.weaponState(1)
    mess = None
    if info[2] <= 0:
        mess = ["EMPTY", CONSTANTS.BLACK, 1, CONSTANTS.RED]
    else:
        mess = [str(info[2]) + "/" + str(info[3]), CONSTANTS.BLACK, 1, CONSTANTS.GREEN]
    if hero.nowWeapon == 1:
        mess[1] = CONSTANTS.GREEN
        mess[2] = 0
    draw_text_box(
        fontSize=15,
        mess="Weapon-1",
        textBoxMidX=182,
        textBoxMidY=CONSTANTS.HEIGHT + 21,
        textBoxWidth=100,
        textBoxHeight=40,
        autoWidth=False,
        autoHeight=False,
        textBoxColor=mess[1],
        textBoxSideWidth=mess[2],
    )
    draw_text_box(
        fontSize=15,
        mess=info[0],
        textBoxMidX=182,
        textBoxMidY=CONSTANTS.HEIGHT + 62,
        textBoxWidth=100,
        textBoxHeight=40,
        autoWidth=False,
        autoHeight=False,
        textBoxColor=mess[1],
        textBoxSideWidth=mess[2],
    )

    drawHealthBar(
        132,
        CONSTANTS.HEIGHT + 82,
        100,
        40,
        info[3],
        info[2],
        color_full=mess[3],
    )
    draw_text_box(
        fontSize=15,
        mess=mess[0],
        textBoxMidX=182,
        textBoxMidY=CONSTANTS.HEIGHT + 103,
        textBoxWidth=100,
        textBoxHeight=40,
        autoWidth=False,
        autoHeight=False,
        textBoxColor=CONSTANTS.BLACK,
        textBoxSideWidth=1,
    )

    info = hero.weaponState(2)
    mess = None
    if info[2] <= 0:
        mess = ["EMPTY", CONSTANTS.BLACK, 1, CONSTANTS.RED]
    else:
        mess = [str(info[2]) + "/" + str(info[3]), CONSTANTS.BLACK, 1, CONSTANTS.GREEN]
    if hero.nowWeapon == 2:
        mess[1] = CONSTANTS.GREEN
        mess[2] = 0
    draw_text_box(
        fontSize=15,
        mess="Weapon-2",
        textBoxMidX=298,
        textBoxMidY=CONSTANTS.HEIGHT + 21,
        textBoxWidth=100,
        textBoxHeight=40,
        autoWidth=False,
        autoHeight=False,
        textBoxColor=mess[1],
        textBoxSideWidth=mess[2],
    )
    draw_text_box(
        fontSize=15,
        mess=info[0],
        textBoxMidX=298,
        textBoxMidY=CONSTANTS.HEIGHT + 62,
        textBoxWidth=100,
        textBoxHeight=40,
        autoWidth=False,
        autoHeight=False,
        textBoxColor=mess[1],
        textBoxSideWidth=mess[2],
    )

    drawHealthBar(
        248,
        CONSTANTS.HEIGHT + 82,
        100,
        40,
        info[3],
        info[2],
        color_full=mess[3],
    )
    draw_text_box(
        fontSize=15,
        mess=mess[0],
        textBoxMidX=298,
        textBoxMidY=CONSTANTS.HEIGHT + 103,
        textBoxWidth=100,
        textBoxHeight=40,
        autoWidth=False,
        autoHeight=False,
        textBoxColor=CONSTANTS.BLACK,
        textBoxSideWidth=1,
    )

    info = hero.weaponState(3)
    mess = None
    if info[2] <= 0:
        mess = ["EMPTY", CONSTANTS.BLACK, 1, CONSTANTS.RED]
    else:
        mess = [str(info[2]) + "/" + str(info[3]), CONSTANTS.BLACK, 1, CONSTANTS.GREEN]
    if hero.nowWeapon == 3:
        mess[1] = CONSTANTS.GREEN
        mess[2] = 0
    draw_text_box(
        fontSize=15,
        mess="Weapon-3",
        textBoxMidX=414,
        textBoxMidY=CONSTANTS.HEIGHT + 21,
        textBoxWidth=100,
        textBoxHeight=40,
        autoWidth=False,
        autoHeight=False,
        textBoxColor=mess[1],
        textBoxSideWidth=mess[2],
    )
    draw_text_box(
        fontSize=15,
        mess=info[0],
        textBoxMidX=414,
        textBoxMidY=CONSTANTS.HEIGHT + 62,
        textBoxWidth=100,
        textBoxHeight=40,
        autoWidth=False,
        autoHeight=False,
        textBoxColor=mess[1],
        textBoxSideWidth=mess[2],
    )

    drawHealthBar(
        364,
        CONSTANTS.HEIGHT + 82,
        100,
        40,
        info[3],
        info[2],
        color_full=mess[3],
    )
    draw_text_box(
        fontSize=15,
        mess=mess[0],
        textBoxMidX=414,
        textBoxMidY=CONSTANTS.HEIGHT + 103,
        textBoxWidth=100,
        textBoxHeight=40,
        autoWidth=False,
        autoHeight=False,
        textBoxColor=CONSTANTS.BLACK,
        textBoxSideWidth=1,
    )
