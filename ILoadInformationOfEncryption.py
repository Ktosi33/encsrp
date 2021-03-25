import abc
import InformationOfEncryption
class ILoadInformationOfEncryption(metaclass = abc.ABCMeta):
    
    @abc.abstractmethod
    def load(self, IOE :InformationOfEncryption):
        pass


