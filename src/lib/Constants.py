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
# 窗口大小
WIDTH, HEIGHT = int(480), int(700)
WINDOWS_SIZE = WIDTH, HEIGHT
# 颜色
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
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
FIRECONTROKEYLIST = [pygame.K_o]
# 单位资源及属性名称
# 通用
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
DEATHIMAGENUM = "DeathImageNum"  # 死亡模型数量
HP = "HP"  # 生命值
# 武器
BULLETSOUND = "BulletSound"  # 射击音效
BULLETSPEED = "BulletSpeed"  # 射速
# 子弹
NORMALBULLET = "normalBullet"  # 普通子弹
# 英雄
HEROAIRCRAFT = "HeroAircraft"  # 英雄
HIGHSPEEDIMAGE = "HighSpeedImage"  # 加速模型
HIGHSPEEDMOVESPEED = "HighSpeedMoveSpeed"  # 加速移动速度增量
HIGHSPEEDMOVEFUEL = "HighSpeedMoveFule"  # 加速移动燃料
