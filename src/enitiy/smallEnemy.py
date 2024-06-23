import copy
import pygame
from pygame.sprite import Group
from pygame.time import Clock
from src.classes.ResourceDict import ResourceDict, AllResourceDict
from src.classes.Aircraft import Aircraft
import src.lib.Constants as CONSTANTS
from src.enitiy.machingGun import MachingGun

class SmallEnemy(Aircraft):
    def __init__(self,x,y):
        super().__init__(
            False,
            CONSTANTS.superResourceDict.getResource(
                CONSTANTS.SMALLENEMY
            ).copyAllResourceDict()
        )
        self.moveTo(x, y)
        self.normalWeapon = MachingGun(False, self.getMidX(), self.Y)
        self.setAutoMove(True)
        self.setAutoDeath(True)
        self.setAutoUseWeapon(True)

    def loadAllResource() -> AllResourceDict:
        allRes = AllResourceDict()
        normalImage = pygame.image.load("images/enemy1.png").convert_alpha()
        allRes.addImage(CONSTANTS.NORMALIMAGE, normalImage)
        deathImage1 = pygame.image.load("images/enemy1_down4.png").convert_alpha()
        allRes.addImage(CONSTANTS.DEATHIMAGEA, deathImage1)
        deathImage2 = pygame.image.load("images/enemy1_down3.png").convert_alpha()
        allRes.addImage(CONSTANTS.DEATHIMAGEB, deathImage2)
        deathImage3 = pygame.image.load("images/enemy1_down2.png").convert_alpha()
        allRes.addImage(CONSTANTS.DEATHIMAGEC, deathImage3)
        deathImage4 = pygame.image.load("images/enemy1_down1.png").convert_alpha()
        allRes.addImage(CONSTANTS.DEATHIMAGED, deathImage4)
        allRes.addValue(CONSTANTS.DEATHIMAGENUM, 4)
        deathSound = pygame.mixer.Sound("sound/enemy1_down.wav")
        deathSound.set_volume(0.2)
        allRes.addSound(CONSTANTS.DEATHSOUND, deathSound)
        allRes.addValue(CONSTANTS.AUTOMOVESPEEDX, 0)
        allRes.addValue(CONSTANTS.AUTOMOVESPEEDY, 1)
        allRes.addValue(CONSTANTS.DAMAGEVALUE, 10)
        allRes.addValue(CONSTANTS.HP, 20)
        allRes.addValue(CONSTANTS.KILLSCORE,5)
        allRes.addValue(CONSTANTS.NAME, "SmallEnemy")
        return allRes
    def hit(self, hitAim):
        super().hit(hitAim)
