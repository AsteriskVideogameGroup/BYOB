from src.model.domain.gamemode import *
from src.utility import MetaSingleton
from src.utility import GlobalSettings


class GameModeFactory(metaclass=MetaSingleton):

    def getGameMode(self, modeid: str) -> IGameMode:
        """
        Translate the gamemode ID in the selected GameMode and add it tho _modes
        :param modeid: String ID of the GameMode
        """

        MODES = 'modes'  # name of the mode setting

        modelist = GlobalSettings().getSetting(MODES)  # list of all available modes

        newmodeclass = globals()[modelist.get(modeid)]  # instantiare the new modality (remember that it's simgleton)

        return newmodeclass()
