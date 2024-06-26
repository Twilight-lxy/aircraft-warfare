import time
import pygame
import src.lib.Constants as CONSTANTS

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


def showLogo(x: int = 0, y: int = (CONSTANTS.HEIGHT / 2 - 100)) -> None:
    logoFont = pygame.font.SysFont(CONSTANTS.DEFALTFONT, 10)
    for i, line in enumerate(LOGO_A):
        text_surface = logoFont.render(line, True, CONSTANTS.BLACK)
        CONSTANTS.screen.blit(text_surface, (x, y + i * 10))


def movingLogoFromTo(
    startX: int = 0,
    startY: int = (CONSTANTS.HEIGHT / 2 - 100),
    endX: int = 0,
    endY: int = 100,
    speed: int = 10,
) -> None:
    CONSTANTS.screen.fill(CONSTANTS.WHITE)
    CONSTANTS.screen.blit(
        CONSTANTS.superResourceDict.getResource(CONSTANTS.BGIMAGE), (0, 0)
    )
    showLogo()
    pygame.display.flip()
    nowX = startX
    nowY = startY
    speedX = (endX - startX) / speed
    speedY = (endY - startY) / speed
    while not (nowX == endX and nowY == endY):
        nowX += speedX
        nowY += speedY
        CONSTANTS.screen.fill(CONSTANTS.WHITE)
        CONSTANTS.screen.blit(
            CONSTANTS.superResourceDict.getResource(CONSTANTS.BGIMAGE), (0, 0)
        )
        showLogo(nowX, nowY)
        pygame.display.flip()
        time.sleep(0.05)
