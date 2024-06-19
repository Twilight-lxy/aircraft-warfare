class ResourceDict:
    resourceDict = dict()

    def __init__(self) -> None:
        self.resourceDict.clear()

    def addResourse(self, resourceName: str, resourceObject: object) -> None:
        if self.resourceDict.get(resourceName, "null") != "null":
            raise ResourceMapException(
                "A resource called " + resourceName + " already exists"
            )
        else:
            self.resourceDict.update({resourceName: resourceObject})

    def getResource(self, resourceName: str) -> object:
        if self.resourceDict.get(resourceName, "null") != "null":
            raise ResourceMapException(
                "A resource called " + resourceName + " does not exist"
            )
        else:
            return self.resourceDict.get(resourceName)

    def removeResource(self, resourceName: str) -> None:
        if self.resourceDict.get(resourceName, "null") != "null":
            raise ResourceMapException(
                "A resource called " + resourceName + " does not exist"
            )
        else:
            self.resourceDict.pop(resourceName)


class ResourceMapException(Exception):
    def __init__(self, info: str) -> None:
        super().__init__(self)
        self.errorinfo = info
