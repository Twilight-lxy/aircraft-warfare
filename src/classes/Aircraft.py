import random
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
        super().__init__(iFF, allRes, X, Y, autoMoveOn, autoMoveSpeedX, autoMoveSpeedY,CONSTANTS.AircraftType)
        if normalWeapon == None:
            normalWeapon = AircraftWeapon(
                iFF, AllResourceDict(), self.getMidX(), self.getMidY()
            )
        self.normalWeapon = normalWeapon
        self.isAutoUseWeapon = isAutoUseWeapon

    def update(self):
        super().update()
        if self.isAutoUseWeapon:
            self.useWeapon(True)

    def useWeapon(self,isAuto:bool=False):
        self.normalWeapon.updateLoadedXY(self.getMidX(), self.getMidY())
        if isAuto:
            nowtime=pygame.time.get_ticks()
            if nowtime - self.normalWeapon.lastOpenFireTick > self.normalWeapon.fireInterval:
                random.seed()
                if random.randint(1,100) > 80:
                    self.normalWeapon.openFire()
                self.normalWeapon.lastOpenFireTick = nowtime
        else:
            self.normalWeapon.openFire()

    def setAutoUseWeapon(self, isAutoUseWeapon: bool):
        self.isAutoUseWeapon = isAutoUseWeapon

    def createCopy(self):
        newCopy=super().createCopy()
        newCopy.__class__ = Aircraft
        return newCopy