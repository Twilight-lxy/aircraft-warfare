from src.classes.ResourceDict import AllResourceDict
import src.lib.Constants as CONSTANTS
from src.classes.AircraftWeapon import AircraftWeapon


class UniversalLauncher(AircraftWeapon):
    def __init__(
        self,
        iFF: bool,
        loadedX: int,
        loadedY: int,
    ) -> None:
        super().__init__(
            iFF,
            CONSTANTS.superResourceDict.getResource(CONSTANTS.UNIVERSALLAUNCHER),
            loadedX,
            loadedY,
        )

    def loadAllResource() -> AllResourceDict:
        allRes = AllResourceDict()
        deathSound = "sound/supply.wav"
        allRes.addSound(CONSTANTS.BULLETSOUND, deathSound)
        allRes.addValue(CONSTANTS.FIREINTERVAL, 5000)
        allRes.addValue(CONSTANTS.NAME, "Bobm Launcher")
        allRes.addValue(CONSTANTS.BULLETNUM, 10)
        return allRes
