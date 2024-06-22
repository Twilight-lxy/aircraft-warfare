import pygame
from src.classes.AircraftWeapon import AircraftWeapon
from src.classes.MobileEntity import MobileEntity
from src.classes.ResourceDict import ResourceDict, AllResourceDict
import src.lib.Constants as CONSTANTS
from pygame.sprite import Group


class Aircraft(MobileEntity):
    def __init__(
        self,
        iFF: bool,
        allRes: AllResourceDict,
        X: int = 0,
        Y: int = 0,
        autoMoveOn: bool = False,
        autoMoveSpeedX: int = 0,
        autoMoveSpeedY: int = 0,
        normalWeapon: AircraftWeapon = None,
        isAutoUseWeapon: bool = False,
    ):
        super().__init__(iFF, allRes, X, Y, autoMoveOn, autoMoveSpeedX, autoMoveSpeedY)
        if normalWeapon == None:
            normalWeapon = AircraftWeapon(
                iFF, AllResourceDict(), self.getMidX(), self.getMidY()
            )
        self.normalWeapon = normalWeapon
        self.isAutoUseWeapon = isAutoUseWeapon

    def update(self,updateLastupdate:bool=True):
        super().update(False)
        if self.isAutoUseWeapon:
            self.useWeapon()
        if(updateLastupdate):
            self.lastupdate = pygame.time.get_ticks()

    def useWeapon(self):
        self.normalWeapon.updateLoadedXY(self.getMidX(), self.getMidY())
        self.normalWeapon.openFire()

    def hit(self, hitAim):
        if hitAim.iFF == self.iFF:
            return
        hitAim.allRes.updateValue(
            CONSTANTS.HP,
            hitAim.allRes.getValue(CONSTANTS.HP)
            - self.allRes.getValue(CONSTANTS.DAMAGEVALUE),
        )

    def setAutoUseWeapon(self, isAutoUseWeapon: bool):
        self.isAutoUseWeapon = isAutoUseWeapon

    def createCopy(self):
        newCopy=super().createCopy()
        newCopy.__class__ = Aircraft
        return newCopy