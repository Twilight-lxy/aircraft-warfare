import pygame
from pygame.sprite import Group
from pygame.time import Clock

from src.classes.ResourceDict import AllResourceDict
from src.classes.MobileEntity import MobileEntity


class WeaponBullet(MobileEntity):
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
        super().__init__(iFF, allRes, X, Y, autoMove, autoMoveSpeedX, autoMoveSpeedY)

    def update(self):
        super().update()
