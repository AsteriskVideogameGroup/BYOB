class ModeMultiton:
    _modes = dict()  # singleton instance

    def __new__(cls, *args, **kwargs) -> 'ModeMultiton':
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
        # import src.domain.gamemanage.gamemode.ModeBuilder as ModeBuilder
        import src.utility.geometrictools.Dimensions as Dimensions

        # call ModeBuilder
        self._environmentobjectfactory = self._objectFactoryBind(modeid)
        self._mapstrategy = self._positionAlgBind(modeid)

        # TODO prendi da database
        self._dimensions = Dimensions(15, 18)
        self._name = "classic"
        self._duration = 300  # 300 secondi
        self._invulnerabilitytime = 3  # secondi
        self._maxplayers = 4  # numero di giocatori della partita

    def getDimensions(self) -> 'Dimensions':
        return self._dimensions

    def setDimensions(self, dim: 'Dimensions'):
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

    def setEnvironmentObjectFactory(self) -> 'IEnvironmentObjectFactory':
        return self._environmentobjectfactory

    def getEnvironmentObjectFactory(self, envobjf: 'IEnvironmentObjectFactory'):
        self._environmentobjectfactory = envobjf

    def setMapStrategy(self) -> 'IMapStrategy':
        return self._mapstrategy

    def getMapStrategy(self, mapstrategy: 'IMapStrategy'):
        self._mapstrategy = mapstrategy

    def _positionAlgBind(self, modeid: str = "classic") -> 'src.utility.mapstrategy.IMapStrategy':
        # list of accepted Map stratiegies
        import src.utility.mapstrategy.FirstMapStrategy as FirstMapStrategy

        import src.utility.settings.GlobalSettings as GlobalSettings
        import src.domain.gamemanage.gamemode.GameModeFactory as GameModeFactory

        mapstrategylist = GlobalSettings().getSetting(GameModeFactory.MAPSTRATEGY)
        # class name of the requested algorithm
        return eval(mapstrategylist.get(modeid))()

    def _objectFactoryBind(self,
                           modeid: str = "classic") -> 'src.domain.gamemanage.environmentobjects.IEnvironmentObjectFactory':  # TODO completa implementazione
        # list of accepted EnvironmentFactories
        import \
            src.domain.gamemanage.environmentobjects.ClassicEnvironmentObjectFactory as ClassicEnvironmentObjectFactory

        import src.utility.settings.GlobalSettings as GlobalSettings
        import src.domain.gamemanage.gamemode.GameModeFactory as GameModeFactory

        envobjlist = GlobalSettings().getSetting(GameModeFactory.ENVOBJFACTORY)
        # class name of the requested environment object factory

        return eval(envobjlist.get(modeid))()


import src.domain.gamemanage.environmentobjects.IEnvironmentObjectFactory as IEnvironmentObjectFactory
import src.utility.mapstrategy.IMapStrategy as IMapStrategy
import src.utility.geometrictools.Dimensions as Dimensions
