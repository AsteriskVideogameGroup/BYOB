from src.model.domain.gamemode.IGameMode import IGameMode
from src.model.domain.gamemode.ClassicMode import ClassicMode


class GameModeFactory:
    def __new__(cls, *args, **kwargs) -> 'GameModeFactory':
        if not hasattr(cls, '_instance'):
            cls._instance = super().__new__(cls)
        return cls._instance

    @classmethod
    def getInstance(cls) -> 'GameModeFactory':
        return cls.__new__(cls)

    def getGameMode(self, modeid: str) -> ClassicMode: # TODO cambiare in IgameMode
        """
        Translate the gamemode ID in the selected GameMode and add it tho _modes

        :param modeid: String ID of the GameMode
        """
        newmodeclass = globals()[modeid]

        return newmodeclass()

