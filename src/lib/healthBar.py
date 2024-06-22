import pygame
import src.lib.Constants as CONSTANTS


def drawHealthBar(
    x,
    y,
    width,
    height,
    fullvalue,
    nowvalue,
    color_empty=CONSTANTS.WHITE,
    color_full=CONSTANTS.GREEN,
):
    # 绘制空血条背景
    pygame.draw.rect(CONSTANTS.screen, color_empty, (x, y, width, height))
    # 根据当前生命值比例绘制满血条
    if(fullvalue == 0):
        full_width=0
    else:
        full_width = width * (nowvalue / fullvalue)
    pygame.draw.rect(CONSTANTS.screen, color_full, (x, y, full_width, height))
