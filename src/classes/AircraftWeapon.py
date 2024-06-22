import copy
import pygame
from pygame.sprite import Group
from src.classes.ResourceDict import AllResourceDict
import src.lib.Constants as CONSTANTS


class AircraftWeapon:
    def __init__(
        self,
        iFF: bool,
        allRes: AllResourceDict,
        loadedX: int,
        loadedY: int,
    ) -> None:
        self.iFF = iFF
        self.allRes = allRes
        self.loadedX = loadedX
        self.loadedY = loadedY
        self.lastOpenFireTick = 0
        self.weaponBullet = None
        self.fullbulltNum = allRes.getValue(CONSTANTS.BULLETNUM)
        self.bulltNum = allRes.getValue(CONSTANTS.BULLETNUM)
    def updateLoadedXY(self, loadedX: int, loadedY: int):
        self.loadedX = loadedX
        self.loadedY = loadedY

    def getNewWeaponBullet(self):
        return self.weaponBullet.createCopy()

    def openFire(self):
        bulletSpeed = self.allRes.getValue(CONSTANTS.FIREINTERVAL)
        nowtime=pygame.time.get_ticks()
        if nowtime - self.lastOpenFireTick > bulletSpeed and self.bulltNum>0:
            newBullet = self.getNewWeaponBullet()
            newBullet.moveTo(self.loadedX,self.loadedY)
            CONSTANTS.weaponBulletGroup.add(newBullet)
            self.lastOpenFireTick = pygame.time.get_ticks()
            self.bulltNum -=1

    def setNewWeaponBullet(self, weaponBullet):
        self.weaponBullet = weaponBullet

    def creatCopy():
        return 