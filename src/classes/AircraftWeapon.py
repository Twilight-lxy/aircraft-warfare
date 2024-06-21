import copy
import pygame
from pygame.sprite import Group


class AircraftWeapon:
    def __init__(self,iFF: bool,weaponBulletGroup: Group,loadedX:int,loadedY:int) -> None:
        self.weaponBulletGroup=weaponBulletGroup
        self.iFF = iFF
        self.loadedX=loadedX
        self.loadedY=loadedY
    def updateLoadedXY(self,loadedX:int,loadedY:int):
        self.loadedX=loadedX
        self.loadedY=loadedY
    def getNewWeaponBullet(self):
        return None
    def openFire(self):
        pass
    def getNewWeaponBullet(self):
        pass
