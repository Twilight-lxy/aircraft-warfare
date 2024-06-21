import pygame
from pygame.sprite import Group
from pygame.time import Clock

from src.classes.ResourceDict import AllResourceDict
from src.classes.AircraftEntity import aircraftEntity


class WeaponBullet(aircraftEntity):
    def __init__(self, iFF: bool, allRes: AllResourceDict, weaponBulletGroup: Group):
        super().__init__(iFF, allRes, weaponBulletGroup)