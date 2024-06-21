import copy
import pygame
from pygame.sprite import Group
from pygame.time import Clock
from src.classes.MobileEntity import MobileEntity
from src.classes.ResourceDict import AllResourceDict, copyAllResourceDict
import src.lib.Constants as CONSTANTS
from src.classes.WeaponBullet import WeaponBullet


class NormalBullet(WeaponBullet):
    def __init__(
        self,
        iFF: bool,
        FireX: int,
        FireY: int,
    ):
        super().__init__(iFF, copyAllResourceDict(CONSTANTS.superResourceDict.getResource(CONSTANTS.NORMALBULLET)), None)
        self.moveTo(FireX, FireY)
        if iFF == True:
            self.allRes.updateValue(CONSTANTS.MOVESPEEDX, self.allRes.getValue(CONSTANTS.MOVESPEEDX) * -1)
            self.allRes.updateValue(CONSTANTS.MOVESPEEDY, self.allRes.getValue(CONSTANTS.MOVESPEEDY) * -1)
        self.setAutoMove(True, self.allRes.getValue(CONSTANTS.MOVESPEEDX), self.allRes.getValue(CONSTANTS.MOVESPEEDY))

    def loadNormalBulletAllResource() -> AllResourceDict:
        allRes = AllResourceDict()
        normalImage = pygame.image.load("images/bullet2.png").convert_alpha()
        allRes.addImage(CONSTANTS.NORMALIMAGE, normalImage)
        allRes.addValue(CONSTANTS.MOVESPEEDX, 0)
        allRes.addValue(CONSTANTS.MOVESPEEDY, 10)
        return allRes

    def hurt(aim: MobileEntity):
        try:
            aim.allRes.updateValue(CONSTANTS.HP, aim.allRes.getValue(CONSTANTS.HP) - 10)
        except:
            pass
