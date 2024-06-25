import pygame
from pygame.sprite import Group
from pygame.time import Clock
from src.classes.ResourceDict import AllResourceDict
import src.lib.Constants as CONSTANTS
from src.classes.AircraftWeapon import AircraftWeapon
from src.enitiy.normalBullet import NormalBullet


class MachingGun(AircraftWeapon):
    def __init__(
        self,
        iFF: bool,
        loadedX: int,
        loadedY: int,
    ) -> None:
        super().__init__(
            iFF,
            CONSTANTS.superResourceDict.getResource(CONSTANTS.MACHINGGUN),
            loadedX,
            loadedY,
        )
        self.setNewWeaponBullet(NormalBullet(self.iFF, self.loadedX, self.loadedY))

    def loadAllResource() -> AllResourceDict:
        allRes = AllResourceDict()
        # deathSound = pygame.mixer.Sound("sound/bullet.wav")
        # deathSound.set_volume(0.5)
        deathSound = "sound/bullet.wav"
        allRes.addSound(CONSTANTS.BULLETSOUND, deathSound)
        allRes.addValue(CONSTANTS.FIREINTERVAL, 100)
        allRes.addValue(CONSTANTS.NAME, "MachingGun")
        allRes.addValue(CONSTANTS.BULLETNUM,1000)
        return allRes
