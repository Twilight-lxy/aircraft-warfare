import pygame
from pygame.sprite import Group
from pygame.time import Clock
from src.classes.ResourceDict import AllResourceDict
import src.lib.Constants as CONSTANTS
from src.classes.AircraftWeapon import AircraftWeapon
from src.enitiy.gunBullet import GunBullet


class UniversalLauncher(AircraftWeapon):
    def __init__(
        self,
        iFF: bool,
        loadedX: int,
        loadedY: int,
    ) -> None:
        super().__init__(
            iFF,
            CONSTANTS.superResourceDict.getResource(CONSTANTS.AIRCRAFTGUN),
            loadedX,
            loadedY,
        )
        self.setNewWeaponBullet(GunBullet(self.iFF, self.loadedX, self.loadedY))

    def loadAllResource() -> AllResourceDict:
        allRes = AllResourceDict()
        deathSound = pygame.mixer.Sound("sound/bullet.wav")
        deathSound.set_volume(1)
        allRes.addSound(CONSTANTS.BULLETSOUND, deathSound)
        allRes.addValue(CONSTANTS.FIREINTERVAL, 1000)
        allRes.addValue(CONSTANTS.NAME, "UniversalLauncher")
        allRes.addValue(CONSTANTS.BULLETNUM,10)
        return allRes
