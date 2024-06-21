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
        weaponBulletGroup:Group,
        X: int = 0,
        Y: int = 0,
        autoMove: bool = False,
        autoMoveSpeedX: int = 0,
        autoMoveSpeedY: int = 0,
        normalWeapon: AircraftWeapon = None,
    ):
        self.weaponBulletGroup=weaponBulletGroup
        super().__init__(iFF, allRes, X, Y, autoMove, autoMoveSpeedX, autoMoveSpeedY)
        if normalWeapon == None:
            normalWeapon = AircraftWeapon(iFF, self.weaponBulletGroup, self.getMidX(), self.getMidY())
        self.normalWeapon = normalWeapon

    def update(self):
        super().update()
        
    def useWeapon(self):
        try:
            self.normalWeapon.updateLoadedXY(self.getMidX(), self.getMidY())
            self.normalWeapon.openFire()
        except:
            pass