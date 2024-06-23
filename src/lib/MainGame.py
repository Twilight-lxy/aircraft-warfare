from queue import Queue
import random
import threading
import time
import pygame
from pygame import Surface
from src.enitiy.addHpBullet import AddHpBullet
from src.lib.DataBaseFunc import addToRankingList
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
    CONSTANTS.aircraftGroup = pygame.sprite.Group()
    CONSTANTS.weaponBulletGroup = pygame.sprite.Group()
    gamePause = False
    queue = Queue()
    addMessQueue = Queue()
    mess = ""
    pygame.mixer.music.play(-1)
    CONSTANTS.screen.fill(CONSTANTS.WHITE)
    hero = Hero()
    # testbullet = NormalBullet(False,100,10)
    CONSTANTS.aircraftGroup.add(hero)
    # CONSTANTS.weaponBulletGroup.add(testbullet)
    # CONSTANTS.aircraftGroup.add(SmallEnemy(200, 20))
    addEnemyThread = threading.Thread(
        target=addEnemy, name="addEnemy", args=(addMessQueue, CONSTANTS.aircraftGroup)
    )
    addEnemyThread.daemon = True
    addEnemyThread.start()
    while True:
        if gamePause:
            try:
                mess = queue.get(True, 0.2)
            except:
                pass
            if mess == "continue":
                mess = ""
                gamePause = False
            if mess == "esc":
                mess = ""
                addMessQueue.put("STOP")
                addEnemyThread.join()
                addToRankingList(GameRecord(username,heroScore,""))
                return username
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
                target=pasueMain, name="pasueMain", args=(queue,)
            )
            pauseThreading.daemon = True
            pauseThreading.start()
            addMessQueue.put(pauseThreading)
        if keymess == "GameOver":
            gamePause = True
            mess = "esc"

        CONSTANTS.weaponBulletGroup.draw(CONSTANTS.screen)
        CONSTANTS.aircraftGroup.draw(CONSTANTS.screen)
        groupCollideAns = pygame.sprite.groupcollide(
            CONSTANTS.aircraftGroup, CONSTANTS.weaponBulletGroup, 0, 0
        )
        for hitFrom, hitlist in groupCollideAns.items():
            for hitaim in hitlist:
                heroScore += doGroupCollode(hitFrom, hitaim,True)
        groupCollideAns = ( pygame.sprite.groupcollide(
            CONSTANTS.aircraftGroup, CONSTANTS.aircraftGroup, 0, 0
        ))
        for hitFrom, hitlist in groupCollideAns.items():
            for hitaim in hitlist:
                heroScore += doGroupCollode(hitFrom, hitaim)
        # print(testsmallenemy.allRes.getValue(CONSTANTS.HP))
        # test = NormalBullet(True,100,10)
        # test.setAutoMove(True,0,10)
        # CONSTANTS.weaponBulletGroup.add(test)
        updateUI(heroScore, hero)
        pygame.display.flip()
        CONSTANTS.mainClock.tick(CONSTANTS.FPS)
        pygame.event.pump()

    return ""


def doGroupCollode(aircraft, bullet, doCanBeBullet:bool=False):
    if aircraft == bullet:
        return 0
    if aircraft.HP > 0:
        if doCanBeBullet and bullet.canBeBullet == False:
            pass
        else:
            aircraft.hit(bullet)
    if aircraft.HP > 0:
        if doCanBeBullet and aircraft.canBeBullet == False:
            pass
        else:
            bullet.hit(aircraft)
    if aircraft.HP <= 0 and aircraft.deathing == -1:
        addScore = aircraft.allRes.getValue(CONSTANTS.KILLSCORE)
        if addScore != -1:
            return addScore
    return 0


def addEnemy(queue:Queue,airGroup):
    lastAddSmallEnemyTime=0
    lastAddAddHpBulletTime=0
    while True:
        time.sleep(0.5)
        mess = None
        nowTime = pygame.time.get_ticks()
        try:
            mess = queue.get(False)
        except:
            pass
        if(mess == "STOP"):
            break
        elif (mess!=None):
            try:
                mess.join()
            except:
                pass
        if len(CONSTANTS.aircraftGroup.sprites())>20:
            time.sleep(0.5)
            continue
        time.sleep(0.5)
        if nowTime-lastAddSmallEnemyTime > 1000:
            random.seed()
            if random.randint(1,100) > 10:
                airGroup.add(SmallEnemy(random.randint(20,CONSTANTS.WIDTH), 20))
            lastAddSmallEnemyTime=nowTime
        time.sleep(0.5)
        if nowTime-lastAddAddHpBulletTime > 1000:
            random.seed()  
            if random.randint(1,100) > 95:
                airGroup.add(AddHpBullet(False,random.randint(20,CONSTANTS.WIDTH), 0))
            lastAddSmallEnemyTime=nowTime

def updateUI(heroScore, hero: Hero):
    draw_text_box(
        fontSize=20,
        mess="    Score:  " + str(heroScore) + "    ",
        textBoxMidX=CONSTANTS.WIDTH - 50,
        textBoxMidY=10,
        textBoxWidth=10,
        textBoxHeight=40,
    )
    pygame.draw.rect(
        CONSTANTS.screen,
        CONSTANTS.WHITE,
        (0, CONSTANTS.HEIGHT, CONSTANTS.WIDTH, CONSTANTS.UIHEIGHT),
    )
    pygame.draw.rect(
        CONSTANTS.screen, CONSTANTS.BLACK, (0, CONSTANTS.HEIGHT, CONSTANTS.WIDTH, 1)
    )
    drawHealthBar(
        1,
        CONSTANTS.HEIGHT + 1,
        100,
        40,
        hero.fullHp,
        hero.HP,
    )
    draw_text_box(
        fontSize=15,
        mess=" HP: " + str(hero.HP),
        textBoxMidX=50,
        textBoxMidY=CONSTANTS.HEIGHT + 21,
        textBoxWidth=100,
        textBoxHeight=40,
        autoWidth=False,
        autoHeight=False,
    )
    drawHealthBar(
        1,
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
        textBoxMidX=50,
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
            1,
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
        textBoxMidX=51,
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
        textBoxMidX=152,
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
        textBoxMidX=152,
        textBoxMidY=CONSTANTS.HEIGHT + 62,
        textBoxWidth=100,
        textBoxHeight=40,
        autoWidth=False,
        autoHeight=False,
        textBoxColor=mess[1],
        textBoxSideWidth=mess[2],
    )

    drawHealthBar(
        102,
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
        textBoxMidX=152,
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
        textBoxMidX=253,
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
        textBoxMidX=253,
        textBoxMidY=CONSTANTS.HEIGHT + 62,
        textBoxWidth=100,
        textBoxHeight=40,
        autoWidth=False,
        autoHeight=False,
        textBoxColor=mess[1],
        textBoxSideWidth=mess[2],
    )

    drawHealthBar(
        204,
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
        textBoxMidX=253,
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
        textBoxMidX=355,
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
        textBoxMidX=355,
        textBoxMidY=CONSTANTS.HEIGHT + 62,
        textBoxWidth=100,
        textBoxHeight=40,
        autoWidth=False,
        autoHeight=False,
        textBoxColor=mess[1],
        textBoxSideWidth=mess[2],
    )

    drawHealthBar(
        305,
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
        textBoxMidX=355,
        textBoxMidY=CONSTANTS.HEIGHT + 103,
        textBoxWidth=100,
        textBoxHeight=40,
        autoWidth=False,
        autoHeight=False,
        textBoxColor=CONSTANTS.BLACK,
        textBoxSideWidth=1,
    )
