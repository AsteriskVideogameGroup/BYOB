import src.domain.gamemanage.player as player
import src.domain.gamemanage.matchmaker as gameessentials
import src.domain.gamemanage.bob as bob


class GameHandler:
    ########## ATTRIBUTES DEFINITION ##########
    # _currentgame : Game
    # _started : Bool

    def __init__(self, newgame: gameessentials.Game):
        """
        :param newgame: Game object to handle
        """
        self._currentgame = newgame
        self._started = False

    def prepareGame(self):
        """ Prepare the game for the start"""

        self._currentgame.prepareGame()
        self._started = self._currentgame.startGame()

    def chooseBoB(self, owner: player.Player, bobnameid: str = 'default'):
        """
        Let the player choose his BoB
        :param owner: Player who choose the BoB
        :param bobnameid: Name id of the chosen BoB
        """
        newbob = bob.BoBBuilder().createBoB(bobnameid, owner)
        self._currentgame.addBoB(newbob)