from src.domain import ClientInfos, MatchMaker
from src.utility import MetaSingleton


class MatchMakingHandler(metaclass=MetaSingleton):

    def makeNewGame(self, client: ClientInfos, modeid: str = 'nomode', isranked: bool = False):
        """
        Request to start a new game
        :param client: Infos of the client of player who wants to start a game
        :param modeid: String ID of the Game Mode
        :param isranked: False if the game is not ranked
        """

        MatchMaker(modeid).pushPlayer(client, isranked)