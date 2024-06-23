import copy
import pygame
from pygame.sprite import Group
from pygame.time import Clock
from src.enitiy.machingGun import MachingGun
from src.classes.ResourceDict import ResourceDict, AllResourceDict
from src.classes.Aircraft import Aircraft
import src.lib.Constants as CONSTANTS
from src.enitiy.aircraftGun import AircraftGun
from src.lib.keyBoard import isDowm


class Hero(Aircraft):
    def __init__(self):
        super().__init__(
            True,
            CONSTANTS.superResourceDict.getResource(
                CONSTANTS.HEROAIRCRAFT
            ).copyAllResourceDict(),
        )
        self.moveTo(CONSTANTS.WIDTH / 2, CONSTANTS.HEIGHT - self.rect.height / 2)
        self.weaponList = [None,MachingGun(True,self.getMidX(), self.getMidY()),AircraftGun(True, self.getMidX(), self.getMidY())]
        self.nowWeapon = 1
        self.normalWeapon = self.weaponList[1]
        self.speed = self.allRes.getValue(CONSTANTS.MOVESPEED)
        self.fullfuel = self.allRes.getValue(CONSTANTS.HIGHSPEEDMOVEFUEL)
        self.fuel = self.allRes.getValue(CONSTANTS.HIGHSPEEDMOVEFUEL)
        self.highSpeedMoveSpeed= self.allRes.getValue(CONSTANTS.HIGHSPEEDMOVESPEED)

    def loadAllResource() -> AllResourceDict:
        allRes = AllResourceDict()
        normalImage = pygame.image.load("images/me2.png").convert_alpha()
        allRes.addImage(CONSTANTS.NORMALIMAGE, normalImage)
        speedImage = pygame.image.load("images/me1.png").convert_alpha()
        allRes.addImage(CONSTANTS.HIGHSPEEDIMAGE, speedImage)
        deathImage1 = pygame.image.load("images/me_destroy_4.png").convert_alpha()
        allRes.addImage(CONSTANTS.DEATHIMAGEA, deathImage1)
        deathImage2 = pygame.image.load("images/me_destroy_3.png").convert_alpha()
        allRes.addImage(CONSTANTS.DEATHIMAGEB, deathImage2)
        deathImage3 = pygame.image.load("images/me_destroy_2.png").convert_alpha()
        allRes.addImage(CONSTANTS.DEATHIMAGEC, deathImage3)
        deathImage4 = pygame.image.load("images/me_destroy_1.png").convert_alpha()
        allRes.addImage(CONSTANTS.DEATHIMAGED, deathImage4)
        allRes.addValue(CONSTANTS.DEATHIMAGENUM, 4)
        deathSound = pygame.mixer.Sound("sound/me_down.wav")
        deathSound.set_volume(0.2)
        allRes.addSound(CONSTANTS.DEATHSOUND, deathSound)
        allRes.addValue(CONSTANTS.MOVESPEED, 5)
        allRes.addValue(CONSTANTS.HIGHSPEEDMOVESPEED, 10)
        allRes.addValue(CONSTANTS.HIGHSPEEDMOVEFUEL, 1000)
        allRes.addValue(CONSTANTS.HP, 1000)
        allRes.addValue(CONSTANTS.DAMAGEVALUE, 10)
        allRes.addValue(CONSTANTS.SCORE, 0)
        allRes.addValue(CONSTANTS.NAME, "Hero")
        return allRes

    def moveByKeyboard(self, keyPressedList):
        if isDowm(CONSTANTS.PAUSECONTROKEYLIST, keyPressedList):
            return "Pause"
        if self.deathing == 0:
            return "GameOver"
        if isDowm(CONSTANTS.WEAPON1CONTROKEYLIST, keyPressedList) and self.weaponState(1)[0]!='None':
            self.nowWeapon = 1
            self.normalWeapon = self.weaponList[1]
        if isDowm(CONSTANTS.WEAPON2CONTROKEYLIST, keyPressedList) and self.weaponState(2)[0]!='None':
            self.nowWeapon = 2
            self.normalWeapon = self.weaponList[2]
        if isDowm(CONSTANTS.WEAPON3CONTROKEYLIST, keyPressedList) and self.weaponState(3)[0]!='None':
            self.nowWeapon = 3
            self.normalWeapon = self.weaponList[3]
        
        self.changeImage(CONSTANTS.NORMALIMAGE)
        ismove = False
        isInHighSpeed = False
        speed = self.speed
        if isDowm(CONSTANTS.HIGHSPEEDCONTROKEYLIST, keyPressedList) and self.fuel > 0:
            speed += self.highSpeedMoveSpeed
            isInHighSpeed = True
        if isDowm(CONSTANTS.LEFTCONTROKEYLIST, keyPressedList):
            self.move(x=self.X - speed)
            ismove = True
        if isDowm(CONSTANTS.RIGHTCONTROKEYLIST, keyPressedList):
            self.move(x=self.X + speed)
            ismove = True
        if isDowm(CONSTANTS.UPCONTROKEYLIST, keyPressedList):
            self.move(y=self.Y - speed)
            ismove = True
        if isDowm(CONSTANTS.DOWNCONTROKEYLIST, keyPressedList):
            self.move(y=self.Y + speed)
            ismove = True
        if isInHighSpeed:
            self.changeImage(CONSTANTS.HIGHSPEEDIMAGE)
            if ismove:
                self.fuel-=1
        if isDowm(CONSTANTS.FIRECONTROKEYLIST, keyPressedList):
            self.useWeapon()

    def useWeapon(self):

        self.normalWeapon.updateLoadedXY(self.getMidX(), self.Y)
        self.normalWeapon.openFire()

    def hit(self, hitAim):
        super().hit(hitAim)

    def weaponState(self, id: int = 0):
        nowtime = pygame.time.get_ticks()
        if id == 0:
            id = self.nowWeapon
        if len(self.weaponList)<id+1:
            return ("None","None",0,0,0,0)
        info = (
            self.weaponList[id].allRes.getValue(CONSTANTS.NAME),
            self.weaponList[id].weaponBullet.allRes.getValue(CONSTANTS.NAME),
            self.weaponList[id].bulltNum,
            self.weaponList[id].fullbulltNum,
            self.weaponList[id].lastOpenFireTick,
            self.weaponList[id].fireInterval,
        )

        return info

    
    def update(self):
        super().update()
        if self.HP<=0:
            self.setAutoDeath(True)