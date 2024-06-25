import pygame
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
    CONSTANTS.threadQueue.put(("loading", "10"))
    backgroundImage = pygame.image.load("images/background.png").convert()
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

    CONSTANTS.threadQueue.put(("loading", "20"))
    # soundResourceDict = src.lib.LoadResource.loadSoundResource()
    CONSTANTS.threadQueue.put(("loading", "100"))
    CONSTANTS.threadQueue.put(("loaded", "100"))

def loadResourceByClassName(CONSTANTSNAME,ClassName):
    CONSTANTS.superResourceDict.addResourse(CONSTANTSNAME,getattr(ClassName,"loadAllResource")())

# def loadSoundResource() -> ResourceDict:
#     resourceDict = ResourceDict()
#     # 射击
#     bullet = pygame.mixer.Sound("sound/bullet.wav")
#     bullet.set_volume(0.2)
#     resourceDict.addResourse("bullet",bullet)
#     # 按钮
#     button = pygame.mixer.Sound("sound/button.wav")
#     button.set_volume(0.2)
#     resourceDict.addResourse("button",button)
#     # 消灭小敌机
#     enemy1_down = pygame.mixer.Sound("sound/enemy1_down.wav")
#     enemy1_down.set_volume(0.2)
#     resourceDict.addResourse("enemy1_down",enemy1_down)
#     # 消灭大敌机
#     enemy2_down = pygame.mixer.Sound("sound/enemy2_down.wav")
#     enemy2_down.set_volume(0.2)
#     resourceDict.addResourse("enemy2_down",enemy2_down)
#     # 消灭BOSS
#     enemy3_down = pygame.mixer.Sound("sound/enemy3_down.wav")
#     enemy3_down.set_volume(0.2)
#     resourceDict.addResourse("enemy3_down",enemy3_down)
#     # BOSS飞行
#     enemy3_fly = pygame.mixer.Sound("sound/enemy3_flying.wav")
#     enemy3_fly.set_volume(0.2)
#     resourceDict.addResourse("enemy3_flying",enemy3_fly)
#     # 获得炸弹
#     get_bomb = pygame.mixer.Sound("sound/get_bomb.wav")
#     get_bomb.set_volume(0.2)
#     resourceDict.addResourse("get_bomb",get_bomb)
#     # 获得子弹
#     get_bullet = pygame.mixer.Sound("sound/get_bullet.wav")
#     get_bullet.set_volume(0.2)
#     resourceDict.addResourse("get_bullet",get_bullet)
#     # 己方坠毁
#     me_down = pygame.mixer.Sound("sound/me_down.wav")
#     me_down.set_volume(0.2)
#     resourceDict.addResourse("me_down",me_down)
#     # 补给
#     supply = pygame.mixer.Sound("sound/supply.wav")
#     supply.set_volume(0.2)
#     resourceDict.addResourse("supply",supply)
#     # 升级
#     upgrade = pygame.mixer.Sound("sound/upgrade.wav")
#     upgrade.set_volume(0.2)
#     resourceDict.addResourse("upgrade",upgrade)
#     # 使用炸弹
#     use_bomb = pygame.mixer.Sound("sound/use_bomb.wav")
#     use_bomb.set_volume(0.2)
#     resourceDict.addResourse("use_bomb",use_bomb)
#     return resourceDict
