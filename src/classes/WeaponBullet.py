from src.classes.ResourceDict import AllResourceDict
from src.classes.MobileEntity import MobileEntity
import src.lib.Constants as CONSTANTS


class WeaponBullet(MobileEntity):
    def __init__(
        self,
        iFF: bool,
        allRes: AllResourceDict,
        X: int = 0,
        Y: int = 0,
        autoMoveOn: bool = False,
        autoMoveSpeedX: int = 0,
        autoMoveSpeedY: int = 0,
    ):
        super().__init__(
            iFF,
            allRes,
            X,
            Y,
            autoMoveOn,
            autoMoveSpeedX,
            autoMoveSpeedY,
            TYPE=CONSTANTS.BulletType,
        )
        self.setAutoDeath(True)

    def update(self):
        super().update()

    def createCopy(self):
        newCopy = super().createCopy()
        newCopy.setAutoDeath(True)
        newCopy.__class__ = WeaponBullet
        return newCopy

    def hit(self, hitAim):
        super().hit(hitAim)
