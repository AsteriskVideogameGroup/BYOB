from src.domain.gamemanage.gamemode import GameModeFactory
from src.utility.metaclasses import MetaSingleton
from src.utility.settings import GlobalSettings


class ModeBuilder(metaclass=MetaSingleton):

    def composeMode(self, mode: 'ModeMultiton', modeid: str):

        """
        Build of the Mode
        :param mode: Mode to be build
        :param modeid: id of the mode
        """
        mode.setEnvironmentObjectFactory(self._objectFactoryBind(modeid))
        mode.setMapStrategy(self._positionAlgBind(modeid))

        self._setStoredAttributes(mode, modeid)


    def positionAlgBind(self, modeid: str = "classic") -> 'src.utility.mapstrategy.IMapStrategy':
        # list of accepted Map stratiegies
        import src.utility.mapstrategy.FirstMapStrategy as FirstMapStrategy

        mapstrategylist = GlobalSettings().getSetting(GameModeFactory.MAPSTRATEGY)
        # class name of the requested algorithm
        return eval(mapstrategylist.get(modeid))()

    def objectFactoryBind(self, modeid: str = "classic") -> 'src.domain.gamemanage.environmentobjects.IEnvironmentObjectFactory': # TODO completa implementazione
        # list of accepted EnvironmentFactories
        import src.domain.gamemanage.environmentobjects.ClassicEnvironmentObjectFactory as ClassicEnvironmentObjectFactory

        envobjlist = GlobalSettings().getSetting(GameModeFactory.ENVOBJFACTORY)
        # class name of the requested environment object factory

        return eval(envobjlist.get(modeid))()

    def _setStoredAttributes(self, mode: 'ModeMultiton', modeid: str):

        import src.utility.geometrictools.Dimensions as Dimensions

        mode.setDimensions(Dimensions(15, 18))
        mode.setName("classic")
        mode.setDuration(300)  # 300 secondi
        mode.setInvulnerabilityTime(3)  # secondi
        mode.setMaxPlayers(4)  # numero di giocatori della partita




import src.domain.gamemanage.environmentobjects.IEnvironmentObjectFactory
import src.utility.mapstrategy.IMapStrategy as IMapStrategy
import src.domain.gamemanage.gamemode.ModeMultiton as ModeMultiton
