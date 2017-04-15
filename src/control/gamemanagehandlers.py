import src.domain.gamemanage.player as player
import src.domain.gamemanage.gameessentials as gameessentials
import src.domain.gamemanage.bob as bob
import src.utility.metaclasses as metaclasses



class MatchMakingHandler(metaclass=metaclasses.MetaSingleton):
    def makeNewGame(self, client: player.ClientInfos, modeid: str = 'nomode', isranked: bool = False):
        """
        Request to start a new game
        :param client: Infos of the client of player who wants to start a game
        :param modeid: String ID of the Game Mode
        :param isranked: False if the game is not ranked
        """

        gameessentials.MatchMaker(modeid).pushPlayer(client, isranked)
