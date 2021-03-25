import abc
import ICryption
import CryptionData
class Cryption:

    def __init__(self, cryptionData : CryptionData, Icryption :ICryption):
        self.cryptionData = cryptionData
        self.Icryption = Icryption

    def Encryption(self):
        pass

    def Decryption(self):
        pass
        
    
    