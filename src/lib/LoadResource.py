import pygame
from src.enitiy.addFuelBullet import AddFuelBullet
from src.enitiy.addBulletBullet import AddBulletBullet
from src.enitiy.universalLauncher import UniversalLauncher
from src.enitiy.bombBullet import BombBullet
from src.enitiy.missileLauncher import MissileLauncher
from src.enitiy.missile import Missile
from src.enitiy.bigEnemy import BigEnemy
from src.enitiy.middleEnemy import MiddleEnemy
from src.enitiy.addHpBullet import AddHpBullet
from src.enitiy.aircraftGun import AircraftGun
from src.enitiy.gunBullet import GunBullet
from src.enitiy.hero import Hero
from src.enitiy.machingGun import MachingGun
from src.enitiy.normalBullet import NormalBullet
from src.enitiy.smallEnemy import SmallEnemy
from src.classes.ResourceDict import ResourceDict
import src.lib.Constants as CONSTANTS


def loadresource():
    CONSTANTS.threadQueue.put(("loading", "0"))
    pygame.mixer.music.load("sound/game_music.ogg")
    pygame.mixer.music.set_volume(0.1)
    backgroundImage = pygame.image.load("images/background.png").convert()
    CONSTANTS.superResourceDict.addResourse(CONSTANTS.BGIMAGE,backgroundImage)
    CONSTANTS.threadQueue.put(("loading", "10"))
    loadResourceByClassName(CONSTANTS.HEROAIRCRAFT,Hero)
    loadResourceByClassName(CONSTANTS.MACHINGGUN,MachingGun)
    loadResourceByClassName(CONSTANTS.AIRCRAFTGUN,AircraftGun)
    loadResourceByClassName(CONSTANTS.MISSILELAUNCHER,MissileLauncher)
    loadResourceByClassName(CONSTANTS.UNIVERSALLAUNCHER,UniversalLauncher)
    loadResourceByClassName(CONSTANTS.NORMALBULLET,NormalBullet)
    loadResourceByClassName(CONSTANTS.GUNBULLET,GunBullet)
    loadResourceByClassName(CONSTANTS.MISSILE,Missile)
    loadResourceByClassName(CONSTANTS.ADDHPBULLET,AddHpBullet)
    loadResourceByClassName(CONSTANTS.BOMBMULLET,BombBullet)
    loadResourceByClassName(CONSTANTS.SMALLENEMY,SmallEnemy)
    loadResourceByClassName(CONSTANTS.MIDDLEENEMY,MiddleEnemy)
    loadResourceByClassName(CONSTANTS.BIGENEMY,BigEnemy)
    loadResourceByClassName(CONSTANTS.ADDBULLETBULLET,AddBulletBullet)
    loadResourceByClassName(CONSTANTS.ADDFUELBULLET,AddFuelBullet)
    CONSTANTS.threadQueue.put(("loading", "20"))
    CONSTANTS.threadQueue.put(("loading", "100"))
    CONSTANTS.threadQueue.put(("loaded", "100"))

def loadResourceByClassName(CONSTANTSNAME,ClassName):
    CONSTANTS.superResourceDict.addResourse(CONSTANTSNAME,getattr(ClassName,"loadAllResource")())
