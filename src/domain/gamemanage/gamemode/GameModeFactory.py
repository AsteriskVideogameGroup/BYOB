from src.domain.gamemanage.gamemode import Mode
from src.utility.metaclasses import MetaSingleton
from src.utility.geometrictools import Dimensions
import src.utility.settings.GlobalSettings as GlobalSettings
import src.utility.mapstrategy.FirstMapStrategy as FirstMapStrategy
import src.domain.gamemanage.environmentobjects.ClassicEnvironmentObjectFactory as ClassicEnvironmentObjectFactory


# TODO gioacchino: ricontrollare sta cosa

class GameModeFactory(metaclass=MetaSingleton):
    MAPSTRATEGY = 'mapstrategy'  # name of the setting that contains all mapstrategy bindings
    ENVOBJFACTORY = 'environmentobjectfactory'  # name of the setting that contains all environment object factory bindings

    def getGameMode(self, modeid: str = "classic"):
        """
        Translate the gamemode ID in the selected GameMode and add it tho _modes
        :param modeid: String ID of the GameMode
        """

        positionalg = self._positionAlgBind(modeid)
        objfactory = self._objectFactoryBind(modeid)

        # TODO dobbiamo prendere i dati da un database

        newmode = Mode(modeid, Dimensions(15, 15), objfactory, positionalg, 4, 3, 300)

        return newmode

    def _positionAlgBind(self, modeid: str = "classic"):
        mapstrategylist = GlobalSettings().getSetting(GameModeFactory.MAPSTRATEGY)
        # class name of the requested algorithm
        return eval(mapstrategylist.get(modeid))()

    def _objectFactoryBind(self, modeid: str = "classic"):  # TODO completa implementazione

        envobjlist = GlobalSettings().getSetting(GameModeFactory.ENVOBJFACTORY)
        # class name of the requested environment object factory

        return eval(envobjlist.get(modeid))()

