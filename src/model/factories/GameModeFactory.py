from src.model.domain.gamemode.IGameMode import IGameMode
from src.model.domain.gamemode.ClassicMode import ClassicMode
from src.model.domain.gamemode.DifferentMode import DifferentMode
from src.utility.GlobalSettings import GlobalSettings


class GameModeFactory:

    def __new__(cls, *args, **kwargs) -> 'GameModeFactory':
        if not hasattr(cls, '_instance'):
            cls._instance = super().__new__(cls)
        return cls._instance

    def getGameMode(self, modeid: str) -> IGameMode:
        """
        Translate the gamemode ID in the selected GameMode and add it tho _modes
        :param modeid: String ID of the GameMode
        """

        MODES = 'modes'  # name of the mode setting
        DEFAULT_MODE = 'default'

        modelist = GlobalSettings().getSetting(MODES)  # list of all available mods

        currentmode = modelist.get(modeid, DEFAULT_MODE)

        newmodeclass = globals()[currentmode]

        return newmodeclass()
