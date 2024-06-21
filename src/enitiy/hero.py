import pygame
from pygame.sprite import Group
from pygame.time import Clock
from src.classes.ResourceDict import ResourceDict, AllResourceDict
from src.classes.AircraftEntity import aircraftEntity
import src.lib.Constants as CONSTANTS
from src.enitiy.aircraftGun import AircraftGun
from src.lib.keyBoard import isDowm
class Hero(aircraftEntity):
    def __init__(
        self, weaponBulletGroup: Group
    ):
        super().__init__(True, CONSTANTS.superResourceDict.getResource(CONSTANTS.HEROAIRCRAFT) , weaponBulletGroup)
        self.moveTo(CONSTANTS.WIDTH / 2, CONSTANTS.HEIGHT - self.rect.height / 2)
        self.normalWeapon = AircraftGun(True,weaponBulletGroup,self.X-self.rect.width,self.Y-self.rect.height)

    def loadHeroAllResource() -> AllResourceDict:
        allRes = AllResourceDict()
        normalImage = pygame.image.load("images/me2.png").convert_alpha()
        allRes.addImage(CONSTANTS.NORMALIMAGE, normalImage)
        speedImage = pygame.image.load("images/me1.png").convert_alpha()
        allRes.addImage(CONSTANTS.HIGHSPEEDIMAGE, speedImage)
        deathImage1 = pygame.image.load("images/me_destroy_1.png").convert_alpha()
        allRes.addImage(CONSTANTS.DEATHIMAGEA, deathImage1)
        deathImage2 = pygame.image.load("images/me_destroy_2.png").convert_alpha()
        allRes.addImage(CONSTANTS.DEATHIMAGEB, deathImage2)
        deathImage3 = pygame.image.load("images/me_destroy_3.png").convert_alpha()
        allRes.addImage(CONSTANTS.DEATHIMAGEC, deathImage3)
        deathImage4 = pygame.image.load("images/me_destroy_4.png").convert_alpha()
        allRes.addImage(CONSTANTS.DEATHIMAGED, deathImage4)
        allRes.addValue(CONSTANTS.DEATHIMAGENUM, 4)
        deathSound = pygame.mixer.Sound("sound/me_down.wav")
        deathSound.set_volume(0.2)
        allRes.addSound(CONSTANTS.DEATHSOUND, deathSound)
        allRes.addValue(CONSTANTS.MOVESPEED, 5)
        allRes.addValue(CONSTANTS.HIGHSPEEDMOVESPEED, 10)
        allRes.addValue(CONSTANTS.HIGHSPEEDMOVEFUEL, 1000)
        allRes.addValue(CONSTANTS.HP,1000)
        return allRes

    def moveByKeyboard(self, keyPressedList):
        self.changeImage(CONSTANTS.NORMALIMAGE)
        speed = self.allRes.getValue(CONSTANTS.MOVESPEED)
        fuel = self.allRes.getValue(CONSTANTS.HIGHSPEEDMOVEFUEL)
        ismove = False
        isInHighSpeed = False
        if isDowm(CONSTANTS.HIGHSPEEDCONTROKEYLIST,keyPressedList) and fuel > 0:
            speed += self.allRes.getValue(CONSTANTS.HIGHSPEEDMOVESPEED)
            isInHighSpeed = True
        if isDowm(CONSTANTS.LEFTCONTROKEYLIST,keyPressedList):
            self.move(x=self.X - speed)
            ismove = True
        if isDowm(CONSTANTS.RIGHTCONTROKEYLIST,keyPressedList):
            self.move(x=self.X + speed)
            ismove = True
        if isDowm(CONSTANTS.UPCONTROKEYLIST,keyPressedList):
            self.move(y=self.Y - speed)
            ismove = True
        if isDowm(CONSTANTS.DOWNCONTROKEYLIST,keyPressedList):
            self.move(y=self.Y + speed)
            ismove = True
        if isInHighSpeed:
            self.changeImage(CONSTANTS.HIGHSPEEDIMAGE)
            if ismove:
                self.allRes.updateValue(CONSTANTS.HIGHSPEEDMOVEFUEL, fuel - 1)
        if(isDowm(CONSTANTS.FIRECONTROKEYLIST,keyPressedList)):
            self.normalWeapon.openfire()

