import abc
from src.model.factories.IEnvironmentObjectFactory import IEnvironmentObjectFactory
from src.utility.Dimensions import Dimensions


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

    @abc.abstractmethod
    def getMaxPlayers(self) -> int:
        """
        Get the number of player who can play contemporary in this mode
        :return:
        """
        pass

    @abc.abstractmethod
    def getDuration(self) -> int:
        """

        :return: duration of each game of the same mode, in minutes
        """
        pass

