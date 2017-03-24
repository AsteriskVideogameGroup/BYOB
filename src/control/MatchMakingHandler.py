from src.model.domain.ClientInfos import ClientInfos
from src.model.domain.MatchMaker import MatchMaker


class MatchMakingHandler:

    def __new__(cls, *args, **kwargs) -> 'MatchMakingHandler':
        if not hasattr(cls, '_instance'):
            cls._instance = super().__new__(cls)
        return cls._instance

    @classmethod
    def getInstance(cls) -> 'MatchMakingHandler':
        return cls.__new__(cls)

    def makeNewGame(self, client: ClientInfos, modeid: str = 'nomode', isranked: bool = False):
        """
        Request to start a new game

        :param client: Infos of the client of player who wants to start a game
        :param modeid: String ID of the Game Mode
        :param isranked: False if the game is not ranked
        """

        MatchMaker(modeid).pushPlayer(client, isranked)
