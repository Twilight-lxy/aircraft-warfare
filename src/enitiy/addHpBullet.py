import copy
import pygame
from pygame.sprite import Group
from pygame.time import Clock
from src.classes.MobileEntity import MobileEntity
from src.classes.ResourceDict import AllResourceDict
import src.lib.Constants as CONSTANTS
from src.classes.WeaponBullet import WeaponBullet


class AddHpBullet(WeaponBullet):
    def __init__(
        self,
        iFF: bool,
        FireX: int,
        FireY: int,
    ):
        super().__init__(iFF, CONSTANTS.superResourceDict.getResource(CONSTANTS.ADDHPBULLET).copyAllResourceDict())
        self.moveTo(FireX, FireY)
        self.setAutoMove(True)
        if iFF == True:
            self.autoMoveSpeedX*=-1
            self.autoMoveSpeedY*=-1
        self.setCanBeBullet(False)

    def loadAllResource() -> AllResourceDict:
        allRes = AllResourceDict()
        normalImage = pygame.image.load("ColorImages/hero/hero_blood.png").convert_alpha()
        allRes.addImage(CONSTANTS.NORMALIMAGE, normalImage)
        allRes.addValue(CONSTANTS.AUTOMOVESPEEDX, 0)
        allRes.addValue(CONSTANTS.AUTOMOVESPEEDY, 7.5)
        allRes.addValue(CONSTANTS.DEATHIMAGENUM, 0)
        allRes.addValue(CONSTANTS.HP, 10)
        allRes.addValue(CONSTANTS.DAMAGEVALUE, 0)
        allRes.addValue(CONSTANTS.NAME, "addHpBullet")
        return allRes

    def hit(self, hitAim):
        hitAim.HP += hitAim.fullHp * 0.1
        if hitAim.HP > hitAim.fullHp:
            hitAim.HP = hitAim.fullHp
        super().hit(hitAim)
    
    def createCopy(self):
        newCopy = super().createCopy()
        newCopy.__class__=AddHpBullet
        return newCopy