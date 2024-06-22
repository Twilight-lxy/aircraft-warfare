import pygame
from pygame import Surface
from src.enitiy.smallEnemy import SmallEnemy
import src.lib.Constants as CONSTANTS
from src.classes.GameRecord import GameRecord
from src.classes.User import User
from src.classes.ResourceDict import ResourceDict
from src.enitiy.hero import Hero
from src.enitiy.normalBullet import NormalBullet
from src.lib.textBox import draw_text_box
from src.lib.healthBar import drawHealthBar


def startGame(username: User) -> GameRecord:
    heroScore = 0
    gameRecord = GameRecord
    CONSTANTS.aircraftGroup = pygame.sprite.Group()
    CONSTANTS.weaponBulletGroup = pygame.sprite.Group()
    gameContinue = True
    pygame.mixer.music.play(-1)
    CONSTANTS.screen.fill(CONSTANTS.WHITE)
    hero = Hero()
    # testbullet = NormalBullet(False,100,10)
    CONSTANTS.aircraftGroup.add(hero)
    # CONSTANTS.weaponBulletGroup.add(testbullet)
    CONSTANTS.aircraftGroup.add(SmallEnemy(200, 20))
    while gameContinue:
        CONSTANTS.screen.fill(CONSTANTS.WHITE)
        CONSTANTS.aircraftGroup.update()
        CONSTANTS.weaponBulletGroup.update()
        for event in pygame.event.get():  # 获取用户事件
            if event.type == pygame.QUIT:  # 如果事件为关闭窗口
                # 退出pygame
                pygame.quit()
                break
        mess = hero.moveByKeyboard(pygame.key.get_pressed())
        if mess == "Pause":
            pass
        if mess == "GameOver":
            gameContinue = False

        CONSTANTS.weaponBulletGroup.draw(CONSTANTS.screen)
        CONSTANTS.aircraftGroup.draw(CONSTANTS.screen)
        groupCollideAns = pygame.sprite.groupcollide(
            CONSTANTS.aircraftGroup, CONSTANTS.weaponBulletGroup, 0, 0
        )
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

    return gameRecord


def doGroupCollode(aircraft, bullet):
    if aircraft.allRes.getValue(CONSTANTS.HP) > 0:
        aircraft.hit(bullet)
        aircraft.update()
    if aircraft.allRes.getValue(CONSTANTS.HP) > 0:
        bullet.hit(aircraft)
        bullet.update()
    if aircraft.allRes.getValue(CONSTANTS.HP) <= 0:
        addScore = aircraft.allRes.getValue(CONSTANTS.KILLSCORE)
        if addScore != -1:
            return addScore
    return 0


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
        CONSTANTS.superResourceDict.getResource(CONSTANTS.HEROAIRCRAFT).getValue(
            CONSTANTS.HP
        ),
        hero.allRes.getValue(CONSTANTS.HP),
    )
    draw_text_box(
        fontSize=15,
        mess=" HP: " + str(hero.allRes.getValue(CONSTANTS.HP)),
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
        CONSTANTS.superResourceDict.getResource(CONSTANTS.HEROAIRCRAFT).getValue(
            CONSTANTS.HIGHSPEEDMOVEFUEL
        ),
        hero.allRes.getValue(CONSTANTS.HIGHSPEEDMOVEFUEL),
        color_full=CONSTANTS.BLUE,
    )
    draw_text_box(
        fontSize=15,
        mess=" FUEL: " + str(hero.allRes.getValue(CONSTANTS.HIGHSPEEDMOVEFUEL)),
        textBoxMidX=50,
        textBoxMidY=CONSTANTS.HEIGHT + 62,
        textBoxWidth=100,
        textBoxHeight=40,
        autoWidth=False,
        autoHeight=False,
    )

    info = hero.weaponState()
    mess = None
    if pygame.time.get_ticks() - info[4] < 10:
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
        textBoxColor=mess[1],
        textBoxSideWidth=mess[2],
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
        textBoxColor=mess[1],
        textBoxSideWidth=mess[2],
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
        textBoxColor=mess[1],
        textBoxSideWidth=mess[2],
    )
