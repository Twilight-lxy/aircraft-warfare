import pygame
from pygame.surface import Surface
from src.lib.typrDefine import ColorType, FontType
from src.lib.Constants import BLACK, WIDTH, DEFALTFONT


# 渲染文本框
def draw_text_box(
    screen: Surface,
    fontName: str = DEFALTFONT,
    fontSize: int = 20,
    mess: str = "",
    textBoxColor: ColorType = BLACK,
    textBoxMidX: float | int = 0,
    textBoxMidY: float | int = 0,
    textBoxWidth: float | int = WIDTH,
    textBoxHeight: float | int = 25,
):
    # 使用字体对象渲染文本
    text_surface = pygame.font.SysFont(fontName, fontSize).render(mess, True, BLACK)

    if(text_surface.get_rect().width > textBoxWidth):
        textBoxWidth = text_surface.get_rect().width
    if(text_surface.get_rect().height > textBoxHeight):
        textBoxHeight = text_surface.get_rect().height
    # 设置文本框颜色
    text_rect = pygame.draw.rect(
        screen, textBoxColor, (textBoxMidX-textBoxWidth/2, textBoxMidY-textBoxHeight/2,textBoxWidth, textBoxHeight), 1
    )

    # 设置文本框内文本的位置
    text_rect.left = textBoxMidX-textBoxWidth/2 + (textBoxWidth - text_surface.get_rect().width) / 2
    text_rect.top = textBoxMidY-textBoxHeight/2 + (textBoxHeight - text_surface.get_rect().height) / 2
    # 绘制文本框
    screen.blit(text_surface, text_rect)
