import ISaveInformationOfEncryption
import ILoadInformationOfEncryption
import InformationOfEncryption
class CryptionData:
    
    def __init__(self,IOE : list, ISIOE : ISaveInformationOfEncryption, ILIOE :ILoadInformationOfEncryption):
        self.informationOfEncryptionList = IOE
        self.IsaveInformationOfEncryption = ISIOE
        self.IloadInformationOfEncryption = ILIOE

