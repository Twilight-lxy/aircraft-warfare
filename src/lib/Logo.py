import time
import pygame
from pygame.surface import Surface
from src.lib.Constants import *

LOGO_A = [
    "",
    "░░░░░░█████╗░██╗██████╗░░█████╗░██████╗░░█████╗░███████╗████████╗░░░░",
    "░░░░░██╔══██╗██║██╔══██╗██╔══██╗██╔══██╗██╔══██╗██╔════╝╚══██╔══╝░░░░",
    "░░░░░███████║██║██████╔╝██║░░╚═╝██████╔╝███████║█████╗░░░░░██║░░░░░░░",
    "░░░░░██╔══██║██║██╔══██╗██║░░██╗██╔══██╗██╔══██║██╔══╝░░░░░██║░░░░░░░",
    "░░░░░██║░░██║██║██║░░██║╚█████╔╝██║░░██║██║░░██║██║░░░░░░░░██║░░░░░░░",
    "░░░░░╚═╝░░╚═╝╚═╝╚═╝░░╚═╝░╚════╝░╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░░░░░░░░╚═╝░░░░░░░",
    "",
    "",
    "░░░░██╗░░░░░░░██╗░█████╗░██████╗░███████╗░█████╗░██████╗░███████╗░░░░",
    "░░░░██║░░██╗░░██║██╔══██╗██╔══██╗██╔════╝██╔══██╗██╔══██╗██╔════╝░░░░",
    "░░░░╚██╗████╗██╔╝███████║██████╔╝█████╗░░███████║██████╔╝█████╗░░░░░░",
    "░░░░░████╔═████║░██╔══██║██╔══██╗██╔══╝░░██╔══██║██╔══██╗██╔══╝░░░░░░",
    "░░░░░╚██╔╝░╚██╔╝░██║░░██║██║░░██║██║░░░░░██║░░██║██║░░██║███████╗░░░░",
    "░░░░░░╚═╝░░░╚═╝░░╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚═╝░░╚═╝╚══════╝░░░░",
    "",
]


def showLogo(screen: Surface, x: int = 0, y: int = (HEIGHT / 2 - 100)) -> None:
    screen.fill(WHITE)
    logoFont = pygame.font.SysFont(DEFALTFONT, 10)
    for i, line in enumerate(LOGO_A):
        text_surface = logoFont.render(line, True, BLACK)
        screen.blit(text_surface, (x, y + i * 10))


def movingLogoFromTo(
    screen: Surface,
    startX: int = 0,
    startY: int = (HEIGHT / 2 - 100),
    endX: int = 0,
    endY: int = 100,
    speed: int = 10,
) -> None:
    showLogo(screen)
    pygame.display.flip()
    nowX = startX
    nowY = startY
    speedX = (endX - startX) / speed
    speedY = (endY - startY) / speed
    while not (nowX == endX and nowY == endY):
        nowX += speedX
        nowY += speedY
        showLogo(screen, nowX, nowY)
        pygame.display.flip()
        time.sleep(0.05)
