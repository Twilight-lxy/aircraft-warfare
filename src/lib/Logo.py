import pygame
from pygame.surface import Surface
from src.lib.Constants import WHITE,BLACK,HEIGHT,DEFALTFONT

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


def showLogo(screen: Surface) -> None:
    screen.fill(WHITE)
    logoFont = pygame.font.SysFont(DEFALTFONT, 10)
    for i, line in enumerate(LOGO_A):
        text_surface = logoFont.render(line, True, BLACK)
        screen.blit(text_surface, (0, HEIGHT / 2 - 100 + i * 10))
