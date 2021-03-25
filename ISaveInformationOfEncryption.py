import abc
import InformationOfEncryption
class ISaveInformationOfEncryption(metaclass = abc.ABCMeta):
    
    @abc.abstractmethod
    def save(self, IOE :InformationOfEncryption):
        pass


