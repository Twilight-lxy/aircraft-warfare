import copy
import pygame
from pygame.sprite import Group
from pygame.time import Clock
from src.classes.MobileEntity import MobileEntity
from src.classes.ResourceDict import AllResourceDict
import src.lib.Constants as CONSTANTS
from src.classes.WeaponBullet import WeaponBullet


class NormalBullet(WeaponBullet):
    def __init__(
        self,
        iFF: bool,
        FireX: int,
        FireY: int,
    ):
        super().__init__(iFF, CONSTANTS.superResourceDict.getResource(CONSTANTS.NORMALBULLET).copyAllResourceDict())
        self.moveTo(FireX, FireY)
        if iFF == True:
            self.allRes.updateValue(CONSTANTS.AUTOMOVESPEEDX, self.allRes.getValue(CONSTANTS.AUTOMOVESPEEDX) * -1)
            self.allRes.updateValue(CONSTANTS.AUTOMOVESPEEDY, self.allRes.getValue(CONSTANTS.AUTOMOVESPEEDY) * -1)
        self.setAutoMove(True)

    def loadNormalBulletAllResource() -> AllResourceDict:
        allRes = AllResourceDict()
        normalImage = pygame.image.load("images/bullet2.png").convert_alpha()
        allRes.addImage(CONSTANTS.NORMALIMAGE, normalImage)
        allRes.addValue(CONSTANTS.AUTOMOVESPEEDX, 0)
        allRes.addValue(CONSTANTS.AUTOMOVESPEEDY, 10)
        allRes.addValue(CONSTANTS.DEATHIMAGENUM, 0)
        allRes.addValue(CONSTANTS.HP, 10)
        allRes.addValue(CONSTANTS.DAMAGEVALUE, 1000)
        allRes.addValue(CONSTANTS.NAME, "Normal")
        return allRes

    def hit(self, hitAim):
        super().hit(hitAim)
    
    def createCopy(self):
        newCopy = super().createCopy()
        newCopy.__class__=NormalBullet
        return newCopy