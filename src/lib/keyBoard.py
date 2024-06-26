def isDowm(keyListName, keyPressedList):
    for i in keyListName:
        if keyPressedList[i]:
            return True
    return False
