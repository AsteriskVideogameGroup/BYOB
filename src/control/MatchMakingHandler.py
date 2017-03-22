from src.model.Player import Player
from src.control.GameHandler import GameHandler


class MatchMakingHandler:

    class __Implementation:

        def __init__(self):
            pass

        def makeNewGame(self, player: Player, modeid: str = 'nomode', isranked: bool = False) -> GameHandler:
            """ Request to join a new Game """
            pass


    _instance: __Implementation = None  # singleton instance

    def __init__(self):
        raise MatchMakingHandler._instance  # throw exception

    @staticmethod
    def getInstance() -> __Implementation:
        if not MatchMakingHandler._instance:
            MatchMakingHandler._instance = MatchMakingHandler.__Implementation()

        return MatchMakingHandler._instance
