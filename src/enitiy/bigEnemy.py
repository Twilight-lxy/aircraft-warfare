import copy
import pygame
from pygame.sprite import Group
from pygame.time import Clock
from src.enitiy.missileLauncher import MissileLauncher
from src.classes.ResourceDict import ResourceDict, AllResourceDict
from src.classes.Aircraft import Aircraft
import src.lib.Constants as CONSTANTS
from src.enitiy.machingGun import MachingGun

class BigEnemy(Aircraft):
    def __init__(self,x,y):
        super().__init__(
            False,
            CONSTANTS.superResourceDict.getResource(
                CONSTANTS.BIGENEMY
            ).copyAllResourceDict()
        )
        self.moveTo(x, y)
        self.normalWeapon = MissileLauncher(False,self.getMidX(),self.getMidY(),CONSTANTS.hero)
        self.setAutoMove(True)
        self.setAutoDeath(True)
        self.setAutoUseWeapon(True)

    def loadAllResource() -> AllResourceDict:
        allRes = AllResourceDict()
        normalImage = pygame.image.load("images/enemy3_hit.png").convert_alpha()
        allRes.addImage(CONSTANTS.NORMALIMAGE, normalImage)
        deathImage1 = pygame.image.load("images/enemy3_down6.png").convert_alpha()
        allRes.addImage(CONSTANTS.DEATHIMAGEA, deathImage1)
        deathImage2 = pygame.image.load("images/enemy3_down5.png").convert_alpha()
        allRes.addImage(CONSTANTS.DEATHIMAGEB, deathImage2)
        deathImage3 = pygame.image.load("images/enemy3_down4.png").convert_alpha()
        allRes.addImage(CONSTANTS.DEATHIMAGEC, deathImage3)
        deathImage4 = pygame.image.load("images/enemy3_down3.png").convert_alpha()
        allRes.addImage(CONSTANTS.DEATHIMAGED, deathImage4)
        deathImage5 = pygame.image.load("images/enemy3_down2.png").convert_alpha()
        allRes.addImage(CONSTANTS.DEATHIMAGEE, deathImage5)
        deathImage6 = pygame.image.load("images/enemy3_down1.png").convert_alpha()
        allRes.addImage(CONSTANTS.DEATHIMAGEF, deathImage6)
        
        allRes.addValue(CONSTANTS.DEATHIMAGENUM, 6)
        # deathSound = pygame.mixer.Sound("sound/enemy1_down.wav")
        # deathSound.set_volume(0.2)
        deathSound = "sound/enemy1_down.wav"
        allRes.addSound(CONSTANTS.DEATHSOUND, deathSound)
        allRes.addValue(CONSTANTS.AUTOMOVESPEEDX, 0)
        allRes.addValue(CONSTANTS.AUTOMOVESPEEDY, 1)
        allRes.addValue(CONSTANTS.DAMAGEVALUE, 20)
        allRes.addValue(CONSTANTS.HP, 400)
        allRes.addValue(CONSTANTS.KILLSCORE,50)
        allRes.addValue(CONSTANTS.NAME, "BigEnemy")
        return allRes
    def hit(self, hitAim):
        super().hit(hitAim)