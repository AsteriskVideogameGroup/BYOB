import Pyro4

from src.domain.gamemanage.gameessentials.MatchMaker import MatchMaker
from src.foundation.metaclasses.MetaSingleton import MetaSingleton
from src.foundation.netmiddleware.NetworkObjectTranslator import NetworkObjectTranslator


@Pyro4.expose
class MatchMakingHandler(metaclass=MetaSingleton):
    def makeNewGame(self, client: str, modeid: str = 'classic', isranked: bool = False):
        """
        Request to start a new game
        :param client: Infos of the client of player who wants to start a game
        :param modeid: String ID of the Game Mode
        :param isranked: False if the game is not ranked
        """

        clientproxy = NetworkObjectTranslator().translate(client)

        MatchMaker(modeid).pushPlayer(clientproxy, isranked)
