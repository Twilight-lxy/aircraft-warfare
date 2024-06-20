import pygame
from pygame import Surface
from src.classes.GameRecord import GameRecord
from src.classes.User import User
from src.classes.ResourceDict import ResourceDict
import src.enitiy.hero
def startGame(screen:Surface,allresource:ResourceDict,mainClock:pygame.time.Clock,username:User) -> GameRecord:
    gameRecord = GameRecord
    aircraftEntityGroup = pygame.sprite.Group
    weaponBulletGroup = pygame.sprite.Group
    gameContinue = True
    pygame.mixer.music.play(-1)
    hero = src.enitiy.hero.crateHero(allresource.getResource("hero"), mainClock ,weaponBulletGroup)
    hero.move(100,500)
    aircraftEntityGroup.add(hero)
    aircraftEntityGroup.draw()
    while gameContinue:
        aircraftEntityGroup.update()
        for event in pygame.event.get():  # 获取用户事件
            if event.type == pygame.QUIT:  # 如果事件为关闭窗口
                # 退出pygame
                pygame.quit()
                break 

    return gameRecord