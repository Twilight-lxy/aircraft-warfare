import math
import pygame
from src.classes.ResourceDict import AllResourceDict
import src.lib.Constants as CONSTANTS
from src.classes.WeaponBullet import WeaponBullet


class BombBullet(WeaponBullet):
    def __init__(
        self,
        iFF: bool,
        FireX: int,
        FireY: int,
    ):
        super().__init__(
            iFF,
            CONSTANTS.superResourceDict.getResource(
                CONSTANTS.BOMBMULLET
            ).copyAllResourceDict(),
        )
        self.moveTo(FireX, FireY)
        self.setAutoMove(True)
        if iFF == True:
            self.autoMoveSpeedX *= -1
            self.autoMoveSpeedY *= -1
        self.setCanBeBullet(True)

    def loadAllResource() -> AllResourceDict:
        allRes = AllResourceDict()
        allRes = AllResourceDict()
        normalImage = pygame.image.load("images/bombonly.png").convert_alpha()
        allRes.addImage(CONSTANTS.NORMALIMAGE, normalImage)
        deathImage1 = pygame.image.load("ColorImages/boom/boom06.png").convert_alpha()
        allRes.addImage(CONSTANTS.DEATHIMAGEA, deathImage1)
        deathImage2 = pygame.image.load("ColorImages/boom/boom05.png").convert_alpha()
        allRes.addImage(CONSTANTS.DEATHIMAGEB, deathImage2)
        deathImage3 = pygame.image.load("ColorImages/boom/boom04.png").convert_alpha()
        allRes.addImage(CONSTANTS.DEATHIMAGEC, deathImage3)
        deathImage4 = pygame.image.load("ColorImages/boom/boom03.png").convert_alpha()
        allRes.addImage(CONSTANTS.DEATHIMAGED, deathImage4)
        deathImage5 = pygame.image.load("ColorImages/boom/boom02.png").convert_alpha()
        allRes.addImage(CONSTANTS.DEATHIMAGEE, deathImage5)
        deathImage6 = pygame.image.load("ColorImages/boom/boom01.png").convert_alpha()
        allRes.addImage(CONSTANTS.DEATHIMAGEF, deathImage6)
        allRes.addValue(CONSTANTS.DEATHIMAGENUM, 6)
        deathSound = "sound/use_bomb.wav"
        allRes.addSound(CONSTANTS.DEATHSOUND, deathSound)
        allRes.addValue(CONSTANTS.AUTOMOVESPEEDX, 0)
        allRes.addValue(CONSTANTS.AUTOMOVESPEEDY, 1)
        allRes.addValue(CONSTANTS.DAMAGEVALUE, 5000)
        allRes.addValue(CONSTANTS.HP, 10)
        allRes.addValue(CONSTANTS.KILLSCORE, 5)
        allRes.addValue(CONSTANTS.NAME, "BombBullet")
        return allRes

    def hit(self, hitAim):
        totScore = 0
        for i in CONSTANTS.allEnemyGroup.sprites():
            if i.iFF != self.iFF:
                if (
                    math.sqrt(
                        (self.getMidX() - i.getMidX()) ** 2
                        + (self.getMidY() - i.getMidY()) ** 2
                    )
                    < 250
                ):
                    i.HP = 0
                    totScore += i.killScore
        super().hit(hitAim)
        hitAim.killScore += totScore

    def createCopy(self):
        newCopy = super().createCopy()
        newCopy.__class__ = BombBullet
        return newCopy

    def update(self):
        super().update()
