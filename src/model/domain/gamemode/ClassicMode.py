from src.model.domain.gamemode.IGameMode import IGameMode
from src.model.factories.IEnvironmentObjectFactory import IEnvironmentObjectFactory
from src.utility.Dimensions import Dimensions


class ClassicMode(IGameMode):

    def __new__(cls, *args, **kwargs) -> 'ClassicMode':
        if not hasattr(cls, '_instance'):
            cls._instance = super().__new__(cls)
        return cls._instance

    @classmethod
    def getInstance(cls) -> 'ClassicMode':
        return cls.__new__(cls)

    def __init__(self):
        self._maxplayer = 4

    def getMaxPlayers(self):
        return self._maxplayer

    def getMapDimensions(self) -> Dimensions:
        """
        :return: map's dimensions for a given mode
        """
        pass

    def getEnvironmentObjectFactory(self) -> IEnvironmentObjectFactory:
        """
        :return: the factory that must produce the environment objects for a given mode
        """
        pass

    def getInvulnerabilityTime(self) -> int:
        """
        :return: the time of invulnerability for a, just damaged, Player
        """
        pass

    def getDuration(self) -> int:
        """

        :return: duration of each game of the same mode, in minutes
        """
        pass
