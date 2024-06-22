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
    ):
        super().__init__(iFF, allRes, X, Y, autoMoveOn, autoMoveSpeedX, autoMoveSpeedY)
        if normalWeapon == None:
            normalWeapon = AircraftWeapon(
                iFF, AllResourceDict(), self.getMidX(), self.getMidY()
            )
        self.normalWeapon = normalWeapon

    def update(self):
        super().update()

    def useWeapon(self):
        try:
            self.normalWeapon.updateLoadedXY(self.getMidX(), self.getMidY())
            self.normalWeapon.openFire()
        except:
            pass
    