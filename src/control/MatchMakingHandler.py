from src.control.GameHandler import *
from src.model.domain.Player import *


class MatchMakingHandler:
    class _Implementation:
        def __init__(self):
            pass

        def makeNewGame(self, player: Player, modeid: str = 'nomode', isranked: bool = False) -> GameHandler:
            """ Request to join a new Game """

            # TODO
            pass

    _instance = None  # singleton instance

    def __init__(self):
        raise SyntaxError  # throw exception

    @classmethod
    def getInstance(cls) -> _Implementation:
        if not cls._instance:
            cls._instance = cls._Implementation()

        return cls._instance
