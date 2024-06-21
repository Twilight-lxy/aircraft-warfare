import pygame
from pygame import Surface
from src.lib.Constants import *
from src.classes.GameRecord import GameRecord
from src.classes.User import User
from src.classes.ResourceDict import ResourceDict
from src.enitiy.Hero import Hero
def startGame(screen:Surface,superResourceDict:ResourceDict,mainClock:pygame.time.Clock,username:User) -> GameRecord:
    gameRecord = GameRecord
    aircraftEntityGroup = pygame.sprite.Group()
    weaponBulletGroup = pygame.sprite.Group()
    gameContinue = True
    pygame.mixer.music.play(-1)
    screen.fill(WHITE)
    hero = Hero(superResourceDict.getResource("hero"), mainClock ,weaponBulletGroup)
    hero.move(0,0)
    aircraftEntityGroup.add(hero)
    aircraftEntityGroup.draw(screen)
    while gameContinue:
        aircraftEntityGroup.update()
        for event in pygame.event.get():  # 获取用户事件
            if event.type == pygame.QUIT:  # 如果事件为关闭窗口
                # 退出pygame
                pygame.quit()
                break
        pygame.display.flip()
        mainClock.tick(FPS)

    return gameRecord