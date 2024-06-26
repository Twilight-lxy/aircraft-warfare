import math
import pygame
from src.classes.ResourceDict import AllResourceDict
import src.lib.Constants as CONSTANTS
from src.classes.WeaponBullet import WeaponBullet


class Missile(WeaponBullet):
    def __init__(
        self,
        iFF: bool,
        FireX: int,
        FireY: int,
        aim=None,
    ):
        super().__init__(
            iFF,
            CONSTANTS.superResourceDict.getResource(
                CONSTANTS.MISSILE
            ).copyAllResourceDict(),
        )
        self.moveTo(FireX, FireY)
        self.setAutoMove(True)
        if iFF == True:
            self.autoMoveSpeedX *= -1
            self.autoMoveSpeedY *= -1
        self.aim = aim
        self.speedX = self.autoMoveSpeedX
        self.speedY = self.autoMoveSpeedY
        self.maxSpeed = self.allRes.getValue(CONSTANTS.MAXMOVESPEED)
        self.maxLockTime = pygame.time.get_ticks() + self.allRes.getValue(
            CONSTANTS.MAXLOCKTIME
        )
        self.image = pygame.transform.rotate(self.image, 180)
        self.baseImage = self.image

    def loadAllResource() -> AllResourceDict:
        allRes = AllResourceDict()
        normalImage = pygame.image.load("ColorImages/bullet/TMD.png").convert_alpha()
        allRes.addImage(CONSTANTS.NORMALIMAGE, normalImage)
        allRes.addValue(CONSTANTS.AUTOMOVESPEEDX, 0)
        allRes.addValue(CONSTANTS.AUTOMOVESPEEDY, 5)
        allRes.addValue(CONSTANTS.DEATHIMAGENUM, 0)
        allRes.addValue(CONSTANTS.HP, 10)
        allRes.addValue(CONSTANTS.DAMAGEVALUE, 200)
        allRes.addValue(CONSTANTS.NAME, "Missile")
        allRes.addValue(CONSTANTS.MAXMOVESPEED, 5)
        allRes.addValue(CONSTANTS.MAXLOCKTIME, 1000)
        return allRes

    def hit(self, hitAim):
        super().hit(hitAim)

    def createCopy(self):
        newCopy = super().createCopy()
        newCopy.__class__ = Missile
        return newCopy

    def setAim(self, aim):
        self.aim = aim

    def autoMove(self):
        if self.aim == None:
            super().autoMove()
        else:
            if self.maxLockTime > pygame.time.get_ticks():
                dx = self.aim.getMidX() - self.getMidX()
                dy = self.aim.getMidY() - self.getMidY()
                try:
                    self.speedX = (
                        self.maxSpeed / (dx * dx + dy * dy) * (dx * dx) * (abs(dx) / dx)
                    )
                    self.speedY = (
                        self.maxSpeed / (dx * dx + dy * dy) * (dy * dy) * (abs(dy) / dy)
                    )
                except:
                    self.speedX = self.autoMoveSpeedX
                    self.speedY = self.autoMoveSpeedY
            self.X += self.speedX
            self.Y += self.speedY
            self.changeAngle()

    def changeAngle(self):
        a = math.atan2(self.speedX, self.speedY)
        angle = a / math.pi * 180
        self.image = pygame.transform.rotate(self.baseImage, angle)
        self.rect = pygame.Rect(self.image.get_rect())
        self.mask = pygame.mask.from_surface(self.image)
        self.move()

    def createCopy(self):
        newCopy = super().createCopy()
        newCopy.aim = self.aim
        newCopy.speedX = self.autoMoveSpeedX
        newCopy.speedY = self.autoMoveSpeedY
        newCopy.maxSpeed = self.maxSpeed
        newCopy.maxLockTime = pygame.time.get_ticks() + self.allRes.getValue(
            CONSTANTS.MAXLOCKTIME
        )
        newCopy.image = pygame.transform.rotate(self.image, 180)
        newCopy.baseImage = self.image
        newCopy.__class__ = Missile
        return newCopy

    def autoDeath(self):
        isOUT = False
        if self.deathing != -1:
            if pygame.time.get_ticks() - self.lastdeath < 30:
                return
        if self.Y + self.rect.height / 2 <= 0:
            isOUT = True
        elif self.Y + self.rect.height / 2 >= CONSTANTS.HEIGHT:
            isOUT = True
        if self.X + self.rect.width / 2 <= 0:
            isOUT = True
        elif self.X + self.rect.width / 2 >= CONSTANTS.WIDTH:
            isOUT = True
        if isOUT or self.HP <= 0:
            self.death()
