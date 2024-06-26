import copy
import pygame
from pygame.sprite import Group
from pygame.time import Clock
from src.classes.MobileEntity import MobileEntity
from src.classes.ResourceDict import AllResourceDict
import src.lib.Constants as CONSTANTS
from src.classes.WeaponBullet import WeaponBullet


class AddBulletBullet(WeaponBullet):
    def __init__(
        self,
        iFF: bool,
        FireX: int,
        FireY: int,
    ):
        super().__init__(
            iFF,
            CONSTANTS.superResourceDict.getResource(
                CONSTANTS.ADDBULLETBULLET
            ).copyAllResourceDict(),
        )
        self.moveTo(FireX, FireY)
        self.setAutoMove(True)
        if iFF == True:
            self.autoMoveSpeedX *= -1
            self.autoMoveSpeedY *= -1
        self.setCanBeBullet(False)

    def loadAllResource() -> AllResourceDict:
        allRes = AllResourceDict()
        normalImage = pygame.image.load("images/bullet_supply.png").convert_alpha()
        allRes.addImage(CONSTANTS.NORMALIMAGE, normalImage)
        allRes.addValue(CONSTANTS.AUTOMOVESPEEDX, 0)
        allRes.addValue(CONSTANTS.AUTOMOVESPEEDY, 7.5)
        allRes.addValue(CONSTANTS.DEATHIMAGENUM, 0)
        allRes.addValue(CONSTANTS.HP, 10)
        allRes.addValue(CONSTANTS.DAMAGEVALUE, 0)
        allRes.addValue(CONSTANTS.NAME, "addBulletBullet")
        return allRes

    def hit(self, hitAim):
        if hitAim.TYPE == CONSTANTS.AircraftType:
            hitAim.normalWeapon.bulltNum += hitAim.normalWeapon.fullbulltNum * 0.1
            if hitAim.normalWeapon.bulltNum > hitAim.normalWeapon.fullbulltNum:
                hitAim.normalWeapon.bulltNum = hitAim.normalWeapon.fullbulltNum
        super().hit(hitAim)

    def createCopy(self):
        newCopy = super().createCopy()
        newCopy.__class__ = AddBulletBullet
        return newCopy
