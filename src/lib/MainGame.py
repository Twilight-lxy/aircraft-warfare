import pygame
from pygame import Surface
from classes.GameRecord import GameRecord
from src.classes.User import User
from src.classes.ResourceDict import ResourceDict
def init():
    pygame.mixer.music.play(-1)
    
def startGame(screen:Surface,allresource:ResourceDict,mainClock:pygame.time.Clock,username:User) -> GameRecord:
    gameRecord = GameRecord

    init()


    return gameRecord