import pygame
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
        super().__init__(
            iFF,
            CONSTANTS.superResourceDict.getResource(
                CONSTANTS.NORMALBULLET
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
        normalImage = pygame.image.load("images/bullet2.png").convert_alpha()
        allRes.addImage(CONSTANTS.NORMALIMAGE, normalImage)
        allRes.addValue(CONSTANTS.AUTOMOVESPEEDX, 0)
        allRes.addValue(CONSTANTS.AUTOMOVESPEEDY, 10)
        allRes.addValue(CONSTANTS.DEATHIMAGENUM, 0)
        allRes.addValue(CONSTANTS.HP, 10)
        allRes.addValue(CONSTANTS.DAMAGEVALUE, 10)
        allRes.addValue(CONSTANTS.NAME, "Normal")
        return allRes

    def hit(self, hitAim):
        super().hit(hitAim)

    def createCopy(self):
        newCopy = super().createCopy()
        newCopy.__class__ = NormalBullet
        return newCopy
