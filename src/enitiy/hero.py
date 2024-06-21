import pygame
from pygame.sprite import Group
from pygame.time import Clock
from src.classes.ResourceDict import ResourceDict, AllResourceDict
from src.classes.AircraftEntity import aircraftEntity
from src.lib.Constants import *

class Hero(aircraftEntity):
    def __init__(self, allRes: AllResourceDict, mainClock: Clock, weaponBulletGroup: Group):
        super().__init__(True, allRes, mainClock, weaponBulletGroup)
        
    def loadHeroAllResource() -> AllResourceDict:
        allRes = AllResourceDict()
        normalImage = pygame.image.load("images/me1.png").convert_alpha()
        allRes.addImage(NORMALIMAGE, normalImage)
        speedImage = pygame.image.load("images/me2.png").convert_alpha()
        allRes.addImage(MOVESPEED, speedImage)
        deathImage1 = pygame.image.load("images/me_destroy_1.png").convert_alpha()
        allRes.addImage(DEATHIMAGEA, deathImage1)
        deathImage2 = pygame.image.load("images/me_destroy_2.png").convert_alpha()
        allRes.addImage(DEATHIMAGEB, deathImage2)
        deathImage3 = pygame.image.load("images/me_destroy_3.png").convert_alpha()
        allRes.addImage(DEATHIMAGEC, deathImage3)
        deathImage4 = pygame.image.load("images/me_destroy_4.png").convert_alpha()
        allRes.addImage(DEATHIMAGED, deathImage4)
        allRes.addValue(DEATHIMAGENUM, 4)
        deathSound = pygame.mixer.Sound("sound/me_down.wav")
        deathSound.set_volume(0.2)
        allRes.addSound(DEATHSOUND, deathSound)
        allRes.addValue(MOVESPEED,10)
        return allRes

    def moveByKeyboard(self,keyValue):
        speed=self.allRes.getValue(MOVESPEED)
        if(keyValue == UPCONTROKEY)
        