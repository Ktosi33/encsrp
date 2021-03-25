import datetime
class InformationOfEncryption:
    def __init__(self, dateOfEncryption, typeOfAlgorithm, typeOfMode, key):
        self._dateOfEncryption = dateOfEncryption
        self._typeOfAlgorithm = typeOfAlgorithm
        self._typeOfMode = typeOfMode
        self._key = key
    
    def getInformationOfEncryption(self):
        return self

