import abc
from src.utile.Dimensions import *
from src.model.IEnvironmentObjectFactory import *

class IGameMode(metaclass=abc.ABCMeta):


    @abc.abstractclassmethod
    def getInstance(cls):
        pass

    @abc.abstractmethod
    def getMapDimensions(self) -> Dimensions:
        pass

    @abc.abstractmethod
    def getEnvironmentObjectFactory(self) -> IEnvironmentObjectFactory:
        pass

    @abc.abstractmethod
    def getInvulnerabilityTime(self) -> int:
        pass

    


