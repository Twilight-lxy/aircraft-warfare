import pygame
from pygame import Surface
import src.lib.Constants as CONSTANTS
from src.classes.GameRecord import GameRecord
from src.classes.User import User
from src.classes.ResourceDict import ResourceDict
from src.enitiy.hero import Hero
from src.enitiy.normalBullet import NormalBullet
def startGame(username:User) -> GameRecord:
    gameRecord = GameRecord
    aircraftEntityGroup = pygame.sprite.Group()
    weaponBulletGroup = pygame.sprite.Group()
    gameContinue = True
    pygame.mixer.music.play(-1)
    CONSTANTS.screen.fill(CONSTANTS.WHITE)
    hero = Hero(weaponBulletGroup)
    testbullet = NormalBullet(False,10,10)
    aircraftEntityGroup.add(hero)
    weaponBulletGroup.add(testbullet)
    while gameContinue:
        CONSTANTS.screen.fill(CONSTANTS.WHITE)
        aircraftEntityGroup.update()
        weaponBulletGroup.update()
        for event in pygame.event.get():  # 获取用户事件
            if event.type == pygame.QUIT:  # 如果事件为关闭窗口
                # 退出pygame
                pygame.quit()
                break
        hero.moveByKeyboard(pygame.key.get_pressed())
        weaponBulletGroup.draw(CONSTANTS.screen)
        aircraftEntityGroup.draw(CONSTANTS.screen)
        pygame.display.flip()
        CONSTANTS.mainClock.tick(CONSTANTS.FPS)

    return gameRecord