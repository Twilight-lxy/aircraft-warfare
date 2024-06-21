import pygame

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
UPCONTROKEY = pygame.K_w
DOWNCONTROKEY = pygame.K_s
LEFTCONTROKEY = pygame.K_a
RIGHTCONTROKEY = pygame.K_d
# 单位资源及属性名称
# 通用
NORMALIMAGE = "NormalImage"  # 基础模型
DEATHIMAGEA = "DeathImageA"  # 死亡模型1
DEATHIMAGEB = "DeathImageB"  # 死亡模型2
DEATHIMAGEC = "DeathImageC"  # 死亡模型3
DEATHIMAGED = "DeathImageD"  # 死亡模型4
DEATHIMAGEE = "DeathImageE"  # 死亡模型5
DEATHIMAGEF = "DeathImageF"  # 死亡模型6
DEATHSOUND = "DeathSoung"  # 死亡音效
MOVESPEED = "MoveSpeed"  # 移动速度
DEATHIMAGENUM = "DeathImageNum"  # 死亡模型数量
# 英雄
