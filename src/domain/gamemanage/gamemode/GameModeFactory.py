from src.domain.gamemanage.environmentobjects import IEnvironmentObjectFactory, ClassicEnvironmentObjectFactory
from src.domain.gamemanage.gamemode import Mode
from src.utility.geometrictools import Dimensions
from src.utility.mapstrategy import IMapStrategy
from src.utility.metaclasses import MetaSingleton
from src.utility.settings import GlobalSettings


class GameModeFactory(metaclass=MetaSingleton):

    MAPSTRATEGY = 'mapstrategy'  # name of the setting that contains all mapstrategy bindings

    def getGameMode(self, modeid: str) -> Mode:
        """
        Translate the gamemode ID in the selected GameMode and add it tho _modes
        :param modeid: String ID of the GameMode
        """

        positionalg = self._positionAlgBind(modeid)
        objfactory = self._objectFactoryBind(modeid)

        # TODO dobbiamo prendere i dati da un database
        newmode = Mode(modeid, Dimensions(15, 15), objfactory, positionalg, 4, 3, 300)

        return newmode

    def _positionAlgBind(self, modeid: str) -> IMapStrategy:
        mapstrategylist = GlobalSettings().getSetting(GameModeFactory.MAPSTRATEGY)
        # class name of the requested algorithm

        return globals()[mapstrategylist.get(modeid)]()  # instantiation

    def _objectFactoryBind(self, modeid: str) -> IEnvironmentObjectFactory: # TODO completa implementazione
        return ClassicEnvironmentObjectFactory()
