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
        autoMove: bool = False,
        autoMoveSpeedX: int = 0,
        autoMoveSpeedY: int = 0,
    ):
        super().__init__()
        self.allRes = allRes
        self.image = self.allRes.getImage(CONSTANTS.NORMALIMAGE)
        self.autoMove = autoMove
        self.autoMoveSpeedX = autoMoveSpeedX
        self.autoMoveSpeedY = autoMoveSpeedY
        self.X = X
        self.Y = Y
        self.rect = pygame.Rect(self.image.get_rect())
        self.iFF = iFF

    def setAutoMove(
        self, autoMove: bool = True, autoMoveSpeedX: int = 0, autoMoveSpeedY: int = 1
    ):
        self.autoMove = autoMove
        self.autoMoveSpeedX = autoMoveSpeedX
        self.autoMoveSpeedY = autoMoveSpeedY

    def moveTo(self, x, y):
        self.X = x - self.rect.width / 2
        self.Y = y - self.rect.height / 2
        self.move()

    def move(self, x: int = -100, y: int = -100):
        if x == -100:
            x = self.X
        if y == -100:
            y = self.Y
        if self.autoMove:
            self.X += self.autoMoveSpeedX
            self.Y += self.autoMoveSpeedY
        else:
            self.X = x
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

    def update(self):
        if self.autoMove:
            self.move()

    def changeImage(self, ImageResourceName):
        self.image = self.allRes.getImage(ImageResourceName)
        self.rect = pygame.Rect(self.image.get_rect())
        self.move()
    def getMidX(self):
        print(type(self.X))
        return int(self.X + self.rect.width/2)
    def getMidY(self):
        return int(self.Y + self.rect.height/2)