import abc
import CryptionData
class ICryption(metaclass = abc.ABCMeta):
    
    @abc.abstractmethod
    def cryption(self, cryptionData :CryptionData):
        pass


