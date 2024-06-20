import pygame


class AircraftWeapon:
    mainClock=None
    def __init__(self,mainClock:pygame.time.Clock) -> None:
        self.mainClock = mainClock