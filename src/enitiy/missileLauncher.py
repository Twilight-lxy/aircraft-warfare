import pygame
from pygame.sprite import Group
from pygame.time import Clock
from src.enitiy.missile import Missile
from src.classes.ResourceDict import AllResourceDict
import src.lib.Constants as CONSTANTS
from src.classes.AircraftWeapon import AircraftWeapon
from src.enitiy.gunBullet import GunBullet
from src.lib.playSound import playSound
class MissileLauncher(AircraftWeapon):
    def __init__(
        self,
        iFF: bool,
        loadedX: int,
        loadedY: int,
        aim
    ) -> None:
        super().__init__(
            iFF,
            CONSTANTS.superResourceDict.getResource(CONSTANTS.MISSILELAUNCHER),
            loadedX,
            loadedY,
        )
        self.setNewWeaponBullet(Missile(False,self.loadedX,self.loadedY,aim))

    def loadAllResource() -> AllResourceDict:
        allRes = AllResourceDict()
        # deathSound = pygame.mixer.Sound("sound/supply.wav")
        # deathSound.set_volume(1)
        deathSound = "sound/supply.wav"
        allRes.addSound(CONSTANTS.BULLETSOUND, deathSound)
        allRes.addValue(CONSTANTS.FIREINTERVAL, 1000)
        allRes.addValue(CONSTANTS.NAME, "MissileLauncher")
        allRes.addValue(CONSTANTS.BULLETNUM,10)
        return allRes
    def openFire(self): 
        nowtime=pygame.time.get_ticks()
        if nowtime - self.lastOpenFireTick > self.fireInterval and self.bulltNum>0:
            newBullet1 = self.getNewWeaponBullet()
            newBullet1.moveTo(self.loadedX-25,self.loadedY)
            newBullet2 = self.getNewWeaponBullet()
            newBullet2.moveTo(self.loadedX+25,self.loadedY)
            CONSTANTS.allEnemyGroup.add(newBullet1)
            CONSTANTS.allEnemyGroup.add(newBullet2)
            if self.isPlaySound:
                try:
                    # CONSTANTS.soundQueue.put(self.fireSound)  
                    # pygame.mixer.find_channel().play(self.fireSound)
                    playSound(self.fireSound)
                except:
                    pass
            self.lastOpenFireTick = pygame.time.get_ticks()
            self.bulltNum -=2
