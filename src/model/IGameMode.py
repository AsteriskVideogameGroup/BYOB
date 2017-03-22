from abc import ABCMeta
from src.utile.Dimensions import *

class IGameMode(metaclass=ABCMeta):

    @ABCMeta.abstractmethod
    def getMapDimensions(self) -> Dimensions:
        pass

    @ABCMeta.abstractmethod
    def getEnvironmentObjectFactory(self) -> :
        pass