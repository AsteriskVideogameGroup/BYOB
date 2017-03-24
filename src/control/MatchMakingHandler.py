from src.control.GameHandler import GameHandler
from src.model.domain.Player import Player


class MatchMakingHandler:

    def __new__(cls, *args, **kwargs) -> 'MatchMakingHandler':
        if not hasattr(cls, '_instance'):
            cls._instance = super().__new__(cls)
        return cls._instance

    @classmethod
    def getInstance(cls) -> 'MatchMakingHandler':
        return cls.__new__(cls)

    def makeNewGame(self, player: Player, modeid: str = 'nomode', isranked: bool = False) -> GameHandler:
        """
        Request to start a new game

        :param player: Player who wants to start a game
        :param modeid: String ID of the Game Mode
        :param isranked: False if the game is not ranked
        """
        pass  # TODO
