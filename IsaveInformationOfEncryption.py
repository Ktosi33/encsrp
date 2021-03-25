import abc
import InformationOfEncryption
class IsaveInformationOfEncryption(metaclass = abc.ABCMeta):
    
    @abc.abstractmethod
    def save(self, ioe :InformationOfEncryption):
        pass


