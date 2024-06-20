import pygame
from src.classes.ResourceDict import ResourceDict, AllResourceDict
from src.classes.AircraftEntity import aircraftEntity


def loadHeroAllResource() -> AllResourceDict:
    allRes = AllResourceDict()
    normalImage = pygame.image.load("images/me1.png").convert_alpha()
    allRes.addImage("normal", normalImage)

    speedImage = pygame.image.load("images/me2.png").convert_alpha()
    allRes.addImage("speed", speedImage)
    deathImage1 = pygame.image.load("images/me_destroy_1.png").convert_alpha()
    allRes.addImage("death1", deathImage1)
    deathImage2 = pygame.image.load("images/me_destroy_2.png").convert_alpha()
    allRes.addImage("death2", deathImage2)
    deathImage3 = pygame.image.load("images/me_destroy_3.png").convert_alpha()
    allRes.addImage("death3", deathImage3)
    deathImage4 = pygame.image.load("images/me_destroy_4.png").convert_alpha()
    allRes.addImage("death4", deathImage4)
    allRes.addValue("deathImageNum", 4)
    deathSound = pygame.mixer.Sound("sound/me_down.wav")
    deathSound.set_volume(0.2)
    allRes.addSound("death", deathSound)
    return allRes


def crateHero(
    allRes: AllResourceDict,
    mainClock: pygame.time.Clock,
    weaponBulletGroup: pygame.sprite.Group,
) -> aircraftEntity:
    hero = aircraftEntity(True, allRes, mainClock, weaponBulletGroup)
    return hero
