import copy
import pygame
from pygame.sprite import Group
from pygame.time import Clock
from src.classes.MobileEntity import MobileEntity
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
        super().__init__(iFF, CONSTANTS.superResourceDict.getResource(CONSTANTS.BOMBMULLET).copyAllResourceDict())
        self.moveTo(FireX, FireY)
        self.setAutoMove(True)
        if iFF == True:
            self.autoMoveSpeedX*=-1
            self.autoMoveSpeedY*=-1
        self.setCanBeBullet(False)
        

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
        # deathSound = pygame.mixer.Sound("sound/enemy1_down.wav")
        # deathSound.set_volume(0.2)
        deathSound = "sound/use_bomb.wav"
        allRes.addSound(CONSTANTS.DEATHSOUND, deathSound)
        allRes.addValue(CONSTANTS.AUTOMOVESPEEDX, 0)
        allRes.addValue(CONSTANTS.AUTOMOVESPEEDY, 0.5)
        allRes.addValue(CONSTANTS.DAMAGEVALUE, 1000)
        allRes.addValue(CONSTANTS.HP, 20)
        allRes.addValue(CONSTANTS.KILLSCORE,5)
        allRes.addValue(CONSTANTS.NAME, "BombBullet")
        return allRes

    def hit(self, hitAim):
        super().hit(hitAim)
    
    def createCopy(self):
        newCopy = super().createCopy()
        newCopy.__class__=BombBullet
        return newCopy
    
    def update(self):
        if self.HP<=0:
            c = Circle((self.getMidX(),self.getMidY()),'red',100,0) 
            c.mask
            for i in CONSTANTS.allEnemyGroup.sprites():
                if i.iFF != self.iFF and i.TYPE != self.TYPE:
                    if c.mask.overlap(i.mask, (c.rect.x- i.getMidX(), c.rect.y - i.getMidY())):
                        i.HP = 0
            
        return super().update()


class Circle():
    def __init__(self,pos,color,radius,width):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((100,100))            #创建1个32X32的Surface实例image
        self.image.set_colorkey((1,2,3))                  #设置image中颜色(1,2,3)的颜色为透明色
        self.image.fill((1, 2, 3))                        #底色为黑色，由于上条，底色变为透明        
        self.radius=radius
        self.width=width
        pygame.draw.circle(self.image,pygame.Color(color),(50,50),self.radius,self.width) #在image上画圆
        self.rect = self.image.get_rect(center=pos)     #rect定义image边界和位置,将image移到指定位置
        self.mask= pygame.mask.from_surface(self.image) #创建记录透明点和不透明点的mask
    def draw(self,aSurface):
        aSurface.blit(self.image,self.rect) #Sprite派生类实例不放入Group,类实例显示需调用自定义draw