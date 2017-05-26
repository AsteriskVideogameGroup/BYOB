from src.domain.gamemanage.gamemode import GameModeFactory
from src.foundation.geometrictools.Dimensions import Dimensions
from src.foundation.settings import GlobalSettings


class ModeMultiton:
    _modes = dict()  # singleton instance

    def __new__(cls, *args, **kwargs):
        if cls._modes.get(args[0], None) is None:
            cls._modes[args[0]] = super().__new__(cls)

        return cls._modes.get(args[0])

    def __init__(self, modeid: str):
        # default initialization
        self._environmentobjectfactory = None
        self._mapstrategy = None
        self._dimensions = None
        self._name = "default"
        self._duration = 0
        self._invulnerabilitytime = 0
        self._maxplayers = 0

        # real initialization
        self._composeMode(modeid)

    def _composeMode(self, modeid: str):

        # call ModeBuilder
        self._environmentobjectfactory = self._objectFactoryBind(modeid)
        self._mapstrategy = self._positionAlgBind(modeid)

        # TODO prendi da database
        self._dimensions = Dimensions(15, 18)
        self._name = "classic"
        self._duration = 300  # 300 secondi
        self._invulnerabilitytime = 3  # secondi
        self._maxplayers = 4  # numero di giocatori della partita

    def getDimensions(self):
        return self._dimensions

    def setDimensions(self, dim):
        self._dimensions = dim

    def getModeName(self) -> str:
        return self._name

    def setModeName(self, modename: str):
        self._name = modename

    def getDuration(self) -> int:
        return self._duration

    def setDuration(self, duration: int):
        self._duration = duration

    def getInvulnerabilityTime(self) -> int:
        return self._invulnerabilitytime

    def setInvulnerabilityTime(self, invtime: int):
        self._invulnerabilitytime = invtime

    def setMaxPlayers(self) -> int:
        return self._maxplayers

    def getMaxPlayers(self, nummaxplayers: int):
        self._maxplayers = nummaxplayers

    def setEnvironmentObjectFactory(self):
        return self._environmentobjectfactory

    def getEnvironmentObjectFactory(self, envobjf):
        self._environmentobjectfactory = envobjf

    def setMapStrategy(self):
        return self._mapstrategy

    def getMapStrategy(self, mapstrategy):
        self._mapstrategy = mapstrategy

    def _positionAlgBind(self, modeid: str = "classic"):
        # list of accepted Map stratiegies

        mapstrategylist = GlobalSettings().getSetting(GameModeFactory.MAPSTRATEGY)
        # class name of the requested algorithm
        return eval(mapstrategylist.get(modeid))()

    def _objectFactoryBind(self, modeid: str = "classic"):  # TODO completa implementazione
        # list of accepted EnvironmentFactories

        envobjlist = GlobalSettings().getSetting(GameModeFactory.ENVOBJFACTORY)
        # class name of the requested environment object factory

        return eval(envobjlist.get(modeid))()


