import pygame

from src.classes.AircraftWeapon import AircraftWeapon
from src.classes.ResourceDict import ResourceDict, AllResourceDict


class aircraftEntity(pygame.sprite.Sprite):
    iFF = False
    autoMove = False
    autoMoveSpeedX = 0
    autoMoveSpeedY = 0
    X = 0
    Y = 0
    normalWeapon = None

    def __init__(
        self,
        iFF: bool,
        allRes: AllResourceDict,
        mainClock: pygame.time.Clock,
        weaponBulletGroup: pygame.sprite.Group,
    ):
        super().__init__()
        self.image = allRes.getImage("normal")

        self.rect = self.image.get_rect()
        self.iFF = iFF
        self.normalWeapon = AircraftWeapon(mainClock)

    def setAutoMove(
        self, autoMove: bool = True, autoMoveSpeedX: int = 0, autoMoveSpeedY: int = 1
    ):
        self.autoMove = autoMove
        self.autoMove = autoMoveSpeedX
        self.autoMoveSpeedY = autoMoveSpeedY

    def move(self, x: int = 0, y: int = 0):
        if self.autoMove:
            self.X += self.autoMoveSpeedX
            self.Y += self.autoMoveSpeedY
        else:
            self.X = x
            self.Y = y

    def update(self):
        self.move()
        # self.rect.move()
        # normalWeapon.use()
