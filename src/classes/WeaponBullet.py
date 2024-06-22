import pygame
from pygame.sprite import Group
from pygame.time import Clock

from src.classes.ResourceDict import AllResourceDict
from src.classes.MobileEntity import MobileEntity
import src.lib.Constants as CONSTANTS


class WeaponBullet(MobileEntity):
    def __init__(
        self,
        iFF: bool,
        allRes: AllResourceDict,
        X: int = 0,
        Y: int = 0,
        autoMoveOn: bool = False,
        autoMoveSpeedX: int = 0,
        autoMoveSpeedY: int = 0,
    ):
        super().__init__(iFF, allRes, X, Y, autoMoveOn, autoMoveSpeedX, autoMoveSpeedY)
        self.setAutoDeath(True)

    def update(self):
        super().update()

    def createCopy(self):
        newCopy = super().createCopy()
        newCopy.setAutoDeath(True)
        newCopy.__class__ = WeaponBullet
        return newCopy

    def hit(self, hitAim):
        if hitAim.iFF == self.iFF:
            return
        hitAim.allRes.updateValue(
            CONSTANTS.HP,
            hitAim.allRes.getValue(CONSTANTS.HP)
            - self.allRes.getValue(CONSTANTS.DAMAGEVALUE),
        )
