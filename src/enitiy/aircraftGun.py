import pygame
from pygame.sprite import Group
from pygame.time import Clock
from src.classes.ResourceDict import AllResourceDict
import src.lib.Constants as CONSTANTS
from src.classes.AircraftWeapon import AircraftWeapon
from src.enitiy.normalBullet import NormalBullet

class AircraftGun(AircraftWeapon):
    def __init__(
        self,
        iFF: bool,
        weaponBulletGroup: Group,
        loadedX: int,
        loadedY: int,
    ) -> None:
        
        super().__init__(iFF, weaponBulletGroup, loadedX, loadedY)

    def loadAircraftGunAllResource() -> AllResourceDict:
        allRes = AllResourceDict()
        deathSound = pygame.mixer.Sound("sound/bullet.wav")
        deathSound.set_volume(0.2)
        allRes.addSound(CONSTANTS.BULLETSOUND, deathSound)
        allRes.addValue(CONSTANTS.BULLETSPEED, 100)
        return allRes
    
    def getNewWeaponBullet(self):
        return NormalBullet(self.iFF,self.loadedX,self.loadedY)
    
    def openFire(self):
        newBullet = self.getNewWeaponBullet()
        self.weaponBulletGroup.add(newBullet)
