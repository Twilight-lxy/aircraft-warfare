import pygame
from pygame.sprite import Group
from pygame.time import Clock
from src.classes.AircraftEntity import aircraftEntity
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
        allRes = CONSTANTS.superResourceDict.getResource(CONSTANTS.NORMALBULLET)
        super().__init__(iFF, allRes, None)
        self.moveTo(FireX, FireY)
        if iFF == True:
            allRes.updateValue(CONSTANTS.MOVESPEEDX, allRes.getValue(CONSTANTS.MOVESPEEDX) * -1)
            allRes.updateValue(CONSTANTS.MOVESPEEDY, allRes.getValue(CONSTANTS.MOVESPEEDY) * -1)
        self.setAutoMove(True, allRes.getValue(CONSTANTS.MOVESPEEDX), allRes.getValue(CONSTANTS.MOVESPEEDY))

    def loadNormalBulletAllResource() -> AllResourceDict:
        allRes = AllResourceDict()
        normalImage = pygame.image.load("images/bullet2.png").convert_alpha()
        allRes.addImage(CONSTANTS.NORMALIMAGE, normalImage)
        allRes.addValue(CONSTANTS.MOVESPEEDX, 0)
        allRes.addValue(CONSTANTS.MOVESPEEDY, 10)
        return allRes

    def hurt(aim: aircraftEntity):
        try:
            aim.allRes.updateValue(CONSTANTS.HP, aim.allRes.getValue(CONSTANTS.HP) - 10)
        except:
            pass
