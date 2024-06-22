import time
import pygame
 
# 初始化Pygame
pygame.init()
 
# 设置屏幕大小和标题
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("血条示例")
 
# 定义一个血条类
class HealthBar(object):
    def __init__(self, x, y, width, height, color_empty, color_full):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color_empty = color_empty
        self.color_full = color_full
        self.value = 100  # 血条初始生命值
 
    def draw(self, surface):
        # 绘制空血条背景
        pygame.draw.rect(surface, self.color_empty, (self.x, self.y, self.width, self.height))
        # 根据当前生命值比例绘制满血条
        full_width = self.width * (self.value / 100)
        pygame.draw.rect(surface, self.color_full, (self.x, self.y, full_width, self.height))
 
# 创建一个血条实例
health_bar = HealthBar(200, 100, 200, 30, (128, 128, 128), (0, 255, 0))
 
running = True
while running:
    # 处理事件
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
 
    # 减少生命值
    health_bar.value -= 1  # 示例减少生命值
    time.sleep(0.5)
    if health_bar.value < 0:
        health_bar.value = 0
 
    # 绘制背景
    screen.fill((255, 255, 255))
 
    # 绘制血条
    health_bar.draw(screen)
 
    # 更新屏幕
    pygame.display.flip()
 
# 退出Pygame
pygame.quit()