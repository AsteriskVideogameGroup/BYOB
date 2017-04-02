from src.model.factories import IEnvironmentObjectFactory
from src.utility import Dimensions, GlobalSettings
from src.utility.mapstrategy import IMapStrategy


class Mode:
    def __init__(self, dimensions: Dimensions, envobjf: IEnvironmentObjectFactory, maxplayers: int, invtime: int, duration: int, name: str):
        self._dimensions = dimensions
        self._environmentobjectfactory = envobjf
        self._maxplayers = maxplayers
        self._invulnerabilitytime = invtime
        self._duration = duration
        self._name = name

        MAPSTRATEGY = 'mapstrategy'
        mapstrategylist = GlobalSettings().getSetting(MAPSTRATEGY)
        self._mapstrategy = globals()[mapstrategylist.get(name)]

    def getMapStrategy(self) -> IMapStrategy:
        """
        :return: map elements' disposal algorithm object
        """
        return self._mapstrategy

    def getMapDimensions(self) -> Dimensions:
        """
        :return: map's dimensions for a given mode
        """
        return self._dimensions

    def getEnvironmentObjectFactory(self) -> IEnvironmentObjectFactory:
        """
        :return: the factory that must produce the environment objects for a given mode
        """
        return self._environmentobjectfactory

    def getInvulnerabilityTime(self) -> int:
        """
        :return: the time of invulnerability for a, just damaged, Player
        """
        return self._invulnerabilitytime

    def getMaxPlayers(self) -> int:
        """
        Get the number of player who can play contemporary in this mode
        :return:
        """
        return self._maxplayers

    def getDuration(self) -> int:
        """

        :return: duration of each game of the same mode, in minutes
        """
        return self._duration
