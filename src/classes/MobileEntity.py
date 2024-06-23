import pygame
from src.classes.ResourceDict import AllResourceDict
import src.lib.Constants as CONSTANTS


class MobileEntity(pygame.sprite.Sprite):

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
        super().__init__()
        self.allRes = allRes
        self.image = self.allRes.getImage(CONSTANTS.NORMALIMAGE)
        self.autoMoveOn = autoMoveOn
        self.autoMoveSpeedX = autoMoveSpeedX
        self.autoMoveSpeedY = autoMoveSpeedY
        self.X = X
        self.Y = Y
        self.rect = pygame.Rect(self.image.get_rect())
        self.iFF = iFF
        self.deathing = -1
        self.autoDeathOn = False
        self.lastdeath = 0
        self.HP = self.allRes.getValue(CONSTANTS.HP)
        self.fullHp = self.allRes.getValue(CONSTANTS.HP)
        self.damageValue=self.allRes.getValue(CONSTANTS.DAMAGEVALUE)
    def setAutoMove(
        self, autoMoveOn: bool = True, autoMoveSpeedX: int = 0, autoMoveSpeedY: int = 0
    ):
        self.autoMoveOn = autoMoveOn
        x = self.allRes.getValue(CONSTANTS.AUTOMOVESPEEDX)
        y = self.allRes.getValue(CONSTANTS.AUTOMOVESPEEDY)
        if x != -1 and autoMoveSpeedX == 0:
            autoMoveSpeedX = x
        if y != -1 and autoMoveSpeedY == 0:
            autoMoveSpeedY = y
        self.autoMoveSpeedX = autoMoveSpeedX
        self.autoMoveSpeedY = autoMoveSpeedY

    def moveTo(self, x, y):
        self.X = x - self.rect.width / 2
        self.Y = y - self.rect.height / 2
        self.move()

    def move(self, x: int = -100, y: int = -100):
        if x != -100:
            self.X = x
        if y != -100:
            self.Y = y
        if self.X + self.rect.width / 2 < 0:
            self.X = 0 - self.rect.width / 2
        elif self.X + self.rect.width / 2 > CONSTANTS.WIDTH:
            self.X = CONSTANTS.WIDTH - self.rect.width / 2
        if self.Y + self.rect.height / 2 < 0:
            self.Y = 0 - self.rect.height / 2
        elif self.Y + self.rect.height / 2 > CONSTANTS.HEIGHT:
            self.Y = CONSTANTS.HEIGHT - self.rect.height / 2
        self.rect.x = self.X
        self.rect.y = self.Y

    def autoMove(self):
        self.X += self.autoMoveSpeedX
        self.Y += self.autoMoveSpeedY
        self.move()

    def update(self):
        if self.autoMoveOn:
            self.autoMove()
        if self.autoDeathOn:
            self.autoDeath()

    def changeImage(self, ImageResourceName):
        self.image = self.allRes.getImage(ImageResourceName)
        self.rect = pygame.Rect(self.image.get_rect())
        self.move()

    def getMidX(self):
        # print(type(self.X))
        return int(self.X + self.rect.width / 2)

    def getMidY(self):
        return int(self.Y + self.rect.height / 2)

    def death(self):
        if self.deathing == -1:
            self.deathing = self.allRes.getValue(CONSTANTS.DEATHIMAGENUM)
            self.allRes.getSound(CONSTANTS.DEATHSOUND).play()
        if self.deathing != -1:
            self.updateDeathImage()

    def updateDeathImage(self):
        if self.deathing == 6:
            self.image = self.allRes.getImage(CONSTANTS.DEATHIMAGEF)
        elif self.deathing == 5:
            self.image = self.allRes.getImage(CONSTANTS.DEATHIMAGEE)
        elif self.deathing == 4:
            self.image = self.allRes.getImage(CONSTANTS.DEATHIMAGED)
        elif self.deathing == 3:
            self.image = self.allRes.getImage(CONSTANTS.DEATHIMAGEC)
        elif self.deathing == 2:
            self.image = self.allRes.getImage(CONSTANTS.DEATHIMAGEB)
        elif self.deathing == 1:
            self.image = self.allRes.getImage(CONSTANTS.DEATHIMAGEA)
        elif self.deathing == 0:
            self.kill()
            return
        self.deathing -= 1
        self.lastdeath = pygame.time.get_ticks()

    def autoDeath(self):
        isOUT = False
        if self.deathing != -1:
            if pygame.time.get_ticks() - self.lastdeath < 30:
                return
        if self.Y + self.rect.height / 2 <= 0:
            isOUT = True
        elif self.Y + self.rect.height / 2 >= CONSTANTS.HEIGHT:
            isOUT = True
        if isOUT or self.HP <= 0:
            self.death()

    def setAutoDeath(self, autoDeath: bool):
        self.autoDeathOn = autoDeath

    def createCopy(self):
        newCopy = MobileEntity(
            self.iFF,
            self.allRes.copyAllResourceDict(),
            self.X,
            self.Y,
            self.autoMoveOn,
            self.autoMoveSpeedX,
            self.autoMoveSpeedY,
        )
        return newCopy

    def hit(self, hitAim):
        if hitAim.iFF == self.iFF:
            return
        hitAim.HP -= self.damageValue