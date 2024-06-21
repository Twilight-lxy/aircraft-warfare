import copy
import pygame


class ResourceDict:

    def __init__(self) -> None:
        self.resourceDict = dict()
        self.clear()

    def addResourse(self, resourceName: str, resourceObject: object) -> None:
        if self.resourceDict.get(resourceName, "null") != "null":
            raise ResourceDictException(
                "A resource called " + resourceName + " already exists"
            )
        else:
            self.resourceDict.update({resourceName: resourceObject})

    def getResource(self, resourceName: str) -> object:
        if self.resourceDict.get(resourceName, "null") == "null":
            raise ResourceDictException(
                "A resource called " + resourceName + " does not exist"
            )
        else:
            return self.resourceDict.get(resourceName)

    def removeResource(self, resourceName: str) -> None:
        if self.resourceDict.get(resourceName, "null") == "null":
            raise ResourceDictException(
                "A resource called " + resourceName + " does not exist"
            )
        else:
            self.resourceDict.pop(resourceName)

    def clear(self) -> None:
        self.resourceDict.clear()

    def updateResource(self, resourceName: str, resourceObject: object) -> None:
        if self.resourceDict.get(resourceName, "null") == "null":
            raise ResourceDictException(
                "A resource called " + resourceName + " does not exist"
            )
        else:
            self.resourceDict.update({resourceName: resourceObject})


class AllResourceDict:

    def __init__(self) -> None:
        self.soundResourceDict = ResourceDict()
        self.imageResourceDict = ResourceDict()
        self.valueResourceDict = ResourceDict()
        self.clearAll()

    def addSound(self, resourceName: str, resourceObject: pygame.mixer.Sound) -> None:
        self.soundResourceDict.addResourse(resourceName, resourceObject)

    def getSound(self, resourceName: str) -> pygame.mixer.Sound:
        return self.soundResourceDict.getResource(resourceName)

    def removeSound(self, resourceName: str) -> None:
        self.soundResourceDict.removeResource(resourceName)

    def addImage(self, resourceName: str, resourceObject: pygame.image) -> None:
        self.imageResourceDict.addResourse(resourceName, resourceObject)

    def getImage(self, resourceName: str) -> pygame.image:
        return self.imageResourceDict.getResource(resourceName)

    def removeImage(self, resourceName: str) -> None:
        self.imageResourceDict.removeResource(resourceName)

    def addValue(self, resourceName: str, resourceObject: object) -> None:
        self.valueResourceDict.addResourse(resourceName, resourceObject)

    def getValue(self, resourceName: str) -> object:
        return self.valueResourceDict.getResource(resourceName)

    def removeValue(self, resourceName: str) -> None:
        self.valueResourceDict.removeResource(resourceName)

    def updateValue(self, resourceName: str, resourceObject: object) -> None:
        self.valueResourceDict.updateResource(resourceName, resourceObject)

    def clearSound(self):
        self.soundResourceDict.clear()

    def clearImage(self):
        self.imageResourceDict.clear()

    def clearValue(self):
        self.valueResourceDict.clear()

    def clearAll(self):
        self.clearImage()
        self.clearSound()
        self.clearValue()

def copyAllResource(fromResourceDict:ResourceDict):
        copyDict = ResourceDict()
        for key,value in fromResourceDict.resourceDict.items():
            copyValue=value
            try:
                copyValue = copy.deepcopy(value)
            except:
                pass
            copyDict.addResourse(key,copyValue)
        return copyDict


def copyAllResourceDict(allResourceDict:AllResourceDict):
    copyAllResourceDict = AllResourceDict()
    copyAllResourceDict.imageResourceDict=copyAllResource(allResourceDict.imageResourceDict)
    copyAllResourceDict.soundResourceDict=copyAllResource(allResourceDict.soundResourceDict)
    copyAllResourceDict.valueResourceDict=copyAllResource(allResourceDict.valueResourceDict)
    return copyAllResourceDict


class ResourceDictException(Exception):
    def __init__(self, info: str) -> None:
        super().__init__(self)
        self.errorinfo = info

    def __str__(self) -> str:
        return self.errorinfo
