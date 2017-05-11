from src.domain.gamemanage.gamemode.Mode import Mode
from src.utility.geometrictools.Dimensions import Dimensions
from src.utility.metaclasses.MetaSingleton import MetaSingleton
from src.utility.settings.GlobalSettings import GlobalSettings

# all possibile MapStrategies
from src.utility.mapstrategy.FirstMapStrategy import FirstMapStrategy

# all possible EnvironmentObjectFactories
from src.domain.gamemanage.environmentobjects.ClassicEnvironmentObjectFactory import ClassicEnvironmentObjectFactory


class ModeBuilder(metaclass=MetaSingleton):
    _MODES_SETTINGS = "modes"

    _NAME = "name"
    _DIMENSIONX = "dimensionsX"
    _DIMENSIONY = "dimensionsY"
    _MAXPLAYERS = "maxplayers"
    _DURATION = "duration"
    _POSITIONALALGO = "positionalalgo"
    _ENVFACTORY = "environmentobjfactory"
    _INVULNERABILITYTIME = "invulnarabilitytime"

    def __init__(self):
        self._buildedmodes = dict()

    def _build(self, modeid: str):
        """
        
        Build mode from configuration

        :param modeid: ID of the mode
        :return: bulded Mode
        """

        # valore di tutti i parametri della modalità da restituire
        # TODO si potrebbe prendere anche da un database, per ora è ok
        jsonselectedmode: dict = GlobalSettings().getSetting(ModeBuilder._MODES_SETTINGS).get(modeid)

        # map dimensions
        dimensionx = jsonselectedmode.get(ModeBuilder._DIMENSIONX)
        dimensiony = jsonselectedmode.get(ModeBuilder._DIMENSIONY)
        mapdimension = Dimensions(dimensionx, dimensiony)

        # mode name
        modename = jsonselectedmode.get(ModeBuilder._NAME)

        # game duration
        duration = jsonselectedmode.get(ModeBuilder._DURATION)

        # positional algorithm
        positionalalgostr = jsonselectedmode.get(ModeBuilder._POSITIONALALGO)
        palgo = eval(positionalalgostr)()

        # environment factory
        envfactorystr = jsonselectedmode.get(ModeBuilder._ENVFACTORY)
        envfactory = eval(envfactorystr)()

        # max players
        maxplayers = jsonselectedmode.get(ModeBuilder._MAXPLAYERS)

        # invulnerability time
        invtime = jsonselectedmode.get(ModeBuilder._INVULNERABILITYTIME)

        # create new mode
        mode = Mode(modename, mapdimension, envfactory, palgo, maxplayers, invtime, duration)

        return mode

    def getMode(self, modeid: str):

        """
        
        Get the selected mode

        :param modeid: ID of the mode
        :return: requested mode
        """
        print(self._buildedmodes)

        if modeid in self._buildedmodes:
            mode = self._buildedmodes.get(modeid)
        else:
            mode = self._build(modeid)
            self._buildedmodes[modeid] = mode

        return mode
