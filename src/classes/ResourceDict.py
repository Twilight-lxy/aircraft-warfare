class ResourceDict:

    def __init__(self) -> None:
        self.resourceDict = dict()
        self.clear()

    def addResourse(self, resourceName: str, resourceObject: any) -> None:
        if self.resourceDict.get(resourceName, "null") != "null":
            raise ResourceDictException(
                "A resource called " + resourceName + " already exists"
            )
        else:
            self.resourceDict.update({resourceName: resourceObject})

    def getResource(self, resourceName: str) -> any:
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


class AllResourceDict:

    def __init__(self) -> None:
        self.soundResourceDict = ResourceDict()
        self.imageResourceDict = ResourceDict()
        self.valueResourceDict = ResourceDict()
        self.clearAll()

    def addSound(self, resourceName: str, resourceObject: any) -> None:
        self.soundResourceDict.addResourse(resourceName, resourceObject)

    def getSound(self, resourceName: str) -> any:
        return self.soundResourceDict.getResource(resourceName)

    def removeSound(self, resourceName: str) -> None:
        self.soundResourceDict.removeResource(resourceName)

    def addImage(self, resourceName: str, resourceObject: any) -> None:
        self.imageResourceDict.addResourse(resourceName, resourceObject)

    def getImage(self, resourceName: str) -> any:
        return self.imageResourceDict.getResource(resourceName)

    def removeImage(self, resourceName: str) -> None:
        self.imageResourceDict.removeResource(resourceName)

    def addValue(self, resourceName: str, resourceObject: any) -> None:
        self.valueResourceDict.addResourse(resourceName, resourceObject)

    def getValue(self, resourceName: str) -> any:
        return self.valueResourceDict.getResource(resourceName)

    def removeValue(self, resourceName: str) -> None:
        self.valueResourceDict.removeResource(resourceName)

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


class ResourceDictException(Exception):
    def __init__(self, info: str) -> None:
        super().__init__(self)
        self.errorinfo = info

    def __str__(self) -> str:
        return self.errorinfo
