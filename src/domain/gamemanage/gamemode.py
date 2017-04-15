import src.domain.gamemanage.mapelements.environmentobjects as environmentobjects
import src.utility.geometrictools as geometrictools
import src.utility.metaclasses as metaclasses
import src.utility.settings.settingmenagers as settings

from src.utility.mapstrategy import *


class Mode:
    ########## ATTRIBUTES DEFINITION ##########
    # _dimensions : Dimensions
    # _environmentobjectfactory : IEnvironmentObjectFactory
    # _maxplayers : Int
    # _invulnerabilitytime : Int
    # _duration : Int
    # _name : String
    # _mapstrategy: IMapStrategy

    def __init__(self, name: str, dimensions: geometrictools.Dimensions,
                 envobjf: environmentobjects.IEnvironmentObjectFactory, positionalgorithm: IMapStrategy,
                 maxplayers: int, invtime: int, duration: int):
        self._dimensions = dimensions
        self._environmentobjectfactory = envobjf
        self._maxplayers = maxplayers
        self._invulnerabilitytime = invtime
        self._duration = duration
        self._name = name
        self._mapstrategy = positionalgorithm

    def getMapStrategy(self) -> IMapStrategy:
        """
        :return: map elements' disposal algorithm object
        """
        return self._mapstrategy

    def getMapDimensions(self) -> geometrictools.Dimensions:
        """ 
        :return: map's dimensions for a given mode
        """
        return self._dimensions

    def getEnvironmentObjectFactory(self) -> environmentobjects.IEnvironmentObjectFactory:
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


class GameModeFactory(metaclass=metaclasses.MetaSingleton):
    MAPSTRATEGY = 'mapstrategy'  # name of the setting that contains all mapstrategy bindings

    def getGameMode(self, modeid: str) -> Mode:
        """
        Translate the gamemode ID in the selected GameMode and add it tho _modes
        :param modeid: String ID of the GameMode
        """

        positionalg = self._positionAlgBind(modeid)
        objfactory = self._objectFactoryBind(modeid)

        # TODO dobbiamo prendere i dati da un database
        newmode = Mode(modeid, geometrictools.Dimensions(15, 15), objfactory, positionalg, 4, 3, 300)

        return newmode

    def _positionAlgBind(self, modeid: str) -> IMapStrategy:
        mapstrategylist = settings.GlobalSettings().getSetting(GameModeFactory.MAPSTRATEGY)
        # class name of the requested algorithm

        return globals()[mapstrategylist.get(modeid)]()  # instantiation

    def _objectFactoryBind(self, modeid: str) -> environmentobjects.IEnvironmentObjectFactory:  # TODO completa implementazione
        return environmentobjects.ClassicEnvironmentObjectFactory()
