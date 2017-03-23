from src.model.factories.IEnvironmentObjectFactory import *
from src.utility.Dimensions import *


class IGameMode(metaclass=abc.ABCMeta):


    @abc.abstractclassmethod
    def getInstance(cls):
        pass

    @abc.abstractmethod
    def getMapDimensions(self) -> Dimensions:
        """

        :return: map's dimensions for a given mode
        """
        pass

    @abc.abstractmethod
    def getEnvironmentObjectFactory(self) -> IEnvironmentObjectFactory:
        """

        :return: the factory that must produce the environment objects for a given mode
        """
        pass

    @abc.abstractmethod
    def getInvulnerabilityTime(self) -> int:
        """

        :return: the time of invulnerability for a, just damaged, Player
        """
        pass




