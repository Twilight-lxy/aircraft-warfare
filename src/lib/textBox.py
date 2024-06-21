import pygame
from pygame.surface import Surface
from src.lib.typrDefine import ColorType, FontType
import src.lib.Constants as CONSTANTS


# 渲染文本框
def draw_text_box(
    fontName: str = CONSTANTS.DEFALTFONT,
    fontSize: int = 20,
    mess: str = "",
    textColor: ColorType = CONSTANTS.BLACK,
    textBoxColor: ColorType = CONSTANTS.BLACK,
    textBoxSideWidth: int = 1,
    textBoxMidX: float | int = 0,
    textBoxMidY: float | int = 0,
    textBoxWidth: float | int = CONSTANTS.WIDTH,
    textBoxHeight: float | int = 25,
):
    # 使用字体对象渲染文本
    text_surface = pygame.font.SysFont(fontName, fontSize).render(mess, True, textColor)

    if text_surface.get_rect().width > textBoxWidth:
        textBoxWidth = text_surface.get_rect().width
    if text_surface.get_rect().height > textBoxHeight:
        textBoxHeight = text_surface.get_rect().height
    # 设置文本位置
    textLeft = (
        textBoxMidX
        - textBoxWidth / 2
        + (textBoxWidth - text_surface.get_rect().width) / 2
    )
    textTop = (
        textBoxMidY
        - textBoxHeight / 2
        + (textBoxHeight - text_surface.get_rect().height) / 2
    )
    # 设置文本框的位置
    textRectLeft = textBoxMidX - textBoxWidth / 2
    textRectTop = textBoxMidY - textBoxHeight / 2
    # 设置文本框
    text_rect = pygame.draw.rect(
        CONSTANTS.screen,
        CONSTANTS.BLACK,
        (textRectLeft, textRectTop, textBoxWidth, textBoxHeight),
        1,
    )
    # 绘制文本框
    pygame.draw.rect(CONSTANTS.screen, textBoxColor, text_rect, textBoxSideWidth)
    # 绘制文本
    CONSTANTS.screen.blit(text_surface, (textLeft, textTop))

    return text_rect
