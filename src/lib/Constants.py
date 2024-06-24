import pygame
from pygame import surface
from pygame.time import Clock
from src.classes.ResourceDict import ResourceDict
from queue import Queue

# 全局变量
superResourceDict: ResourceDict
screen: pygame.display.set_mode
threadQueue: Queue
mainClock: Clock
weaponBulletGroup: pygame.sprite.Group
aircraftGroup: pygame.sprite.Group
hero = None
# 窗口大小
WIDTH, HEIGHT = int(480), int(700)
UIHEIGHT = int(123)
WINDOWS_SIZE = WIDTH, HEIGHT + UIHEIGHT
# 颜色
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
# 默认字体
DEFALTFONT = "Times_New_Roman"
# 页面FPS
FPS = int(60)
# 操作按键定义
UPCONTROKEYLIST = [pygame.K_w, pygame.K_UP]
DOWNCONTROKEYLIST = [pygame.K_s, pygame.K_DOWN]
LEFTCONTROKEYLIST = [pygame.K_a, pygame.K_LEFT]
RIGHTCONTROKEYLIST = [pygame.K_d, pygame.K_RIGHT]
HIGHSPEEDCONTROKEYLIST = [pygame.K_LSHIFT, pygame.K_RSHIFT]
FIRECONTROKEYLIST = [pygame.K_j]
PAUSECONTROKEYLIST = [pygame.K_ESCAPE]
WEAPON1CONTROKEYLIST = [pygame.K_1]
WEAPON2CONTROKEYLIST = [pygame.K_2]
WEAPON3CONTROKEYLIST = [pygame.K_3]

# 单位资源及属性名称
# 通用
NAME = "Name"  # 名称
NORMALIMAGE = "NormalImage"  # 基础模型
DEATHIMAGEA = "DeathImageA"  # 死亡模型1
DEATHIMAGEB = "DeathImageB"  # 死亡模型2
DEATHIMAGEC = "DeathImageC"  # 死亡模型3
DEATHIMAGED = "DeathImageD"  # 死亡模型4
DEATHIMAGEE = "DeathImageE"  # 死亡模型5
DEATHIMAGEF = "DeathImageF"  # 死亡模型6
DEATHSOUND = "DeathSound"  # 死亡音效
MOVESPEED = "MoveSpeed"  # XY移动速度
MOVESPEEDX = "MoveSpeedX"  # X移动速度
MOVESPEEDY = "MoveSpeedY"  # Y移动速度
MAXMOVESPEED = "MaxMoveSpeed" # 最大总移动速度
AUTOMOVESPEEDX = "AutoMoveSpeedX"  # X自动移动速度
AUTOMOVESPEEDY = "AutoMoveSpeedY"  # Y自动移动速度
DEATHIMAGENUM = "DeathImageNum"  # 死亡模型数量
HP = "HP"  # 生命值
KILLSCORE = "KillScore"  # 分值
SCORE = "Score"  # 得分
# 武器
BULLETSOUND = "BulletSound"  # 射击音效
FIREINTERVAL = "FireInterval"  # 射速
AIRCRAFTGUN = "AircraftGun"
MACHINGGUN = "MachingGun"
BULLETNUM = "BulletNum"
UNIVERSALLAUNCHER = "universalLauncher"
MISSILELAUNCHER = "MissileLauncher"
MAXLOCKTIME = "MaxLockTime"
# 子弹
NORMALBULLET = "normalBullet"  # 普通子弹
GUNBULLET = "GunBullet"
DAMAGEVALUE = "DamageValue"  # 伤害
ADDHPBULLET = "AddHpBullet"
MISSILE = "Missile"
# 英雄
HEROAIRCRAFT = "HeroAircraft"  # 英雄
HIGHSPEEDIMAGE = "HighSpeedImage"  # 加速模型
HIGHSPEEDMOVESPEED = "HighSpeedMoveSpeed"  # 加速移动速度增量
HIGHSPEEDMOVEFUEL = "HighSpeedMoveFule"  # 加速移动燃料
# 敌人
SMALLENEMY = "SmallEnemy"  # 小型敌人
MIDDLEENEMY = "MiddleEnemy" #中型敌人
BIGENEMY = "BigEnemy"  # 大型敌人
